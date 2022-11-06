#Kirin Hardinger
#CS 457 Fall 2022
#Project 2
#table.py

""" HISTORY

October 24:
    Created table.py
    Took table-related commands from helper.py and put them into table.py
    Created insert functionality

October 29:
    Created update functionality
    Created delete functionality
    Created select functionality with specified columns
    
"""

import helper
import os

def createTable(cwd, command):
    #separate table name
    table_name = helper.removePhrase(command, "create table ")
    table_name = table_name.split()[0]

    #separate table contents and replace commas, remove extra ()s
    table_contents = helper.removePhrase(command, "create table " + table_name + " ")
    table_contents = table_contents.replace(",", " |")
    if(table_contents[0] == '(' and table_contents[-1] == ')'):
        table_contents = table_contents[1:-1]

    #set path and create table if it doesn't already exist
    newpath = cwd + "/" + table_name

    if(not os.path.exists(newpath)):
        with open(table_name, 'w') as f:
            f.write(table_contents)
        print("Table " + table_name + " created.")
    else:
        print(helper.bcolors.RED + "!Failed to create table " + table_name + " because it already exists." + helper.bcolors.END)

def dropTable(cwd, command):
    #set table name and path
    table_name = helper.removePhrase(command, "drop table ")
    newpath = cwd + "/" + table_name

    #check if table exists
    #if so, delete the file
    if(os.path.exists(newpath)):
        os.remove(newpath)
        print("Table " + table_name + " deleted.")
    else:
        print(helper.bcolors.RED + "!Failed to delete table " + table_name + " because it does not exist." + helper.bcolors.END)

#displays all values in table
def selectAll(cwd, command):
    #set table name and path
    table_name = helper.removePhrase(command, "select * from ")
    newpath = cwd + "/" + table_name

    #check if table exists
    #if so, print out all comments
    if(os.path.exists(newpath)):
        with open(newpath, 'r') as f:
            print("")
            print(f.read())
    else:
        print(helper.bcolors.RED + "!Failed to query table " + table_name + " because it does not exist." + helper.bcolors.END)

#displays specific values in table given specified columns
def select(cwd, command):
    #remove "select " from phrase
    command = helper.removePhrase(command, "select ")
    
    #separate table name and columns
    columns = command.split("from", 1)[0]
    columns = columns.split(",")

    for x in range(len(columns)):
        columns[x] = columns[x].replace(" ", '')
        command = helper.removePhrase(command, columns[x])

    command = helper.removePhrase(command, ",  from ")
    table_name = command.split(" ", 1)[0]

    #ensures table exists
    newpath = cwd + "/" + table_name
    if not os.path.exists(newpath):
        print(helper.bcolors.RED + "!Failed to query " + table_name + " because it does not exist." + helper.bcolors.END)
        return

    command = helper.removePhrase(command, table_name + " where ")

    #separate selected columns
    selected_column = command.split(" ", 1)[0]
    command = helper.removePhrase(command, selected_column + " ")

    #separate operator
    operator_str = command.split(" ", 1)[0]
    command = helper.removePhrase(command, operator_str + " ")

    #separate comparison value
    comp_value = command
    comp_value = comp_value.replace(" ", '')

    with open(table_name, 'r') as f:
        lines = f.readlines()

    print("")

    #open table file for reading, find index of selected column
    with open(table_name, 'r') as f:
        attributes = f.readline().strip().split(" | ")

    #find index of selected column for setting
    index = 0
    found = False
    for i in range(len(attributes)):
        if attributes[i] == selected_column and not found:
            found = True
            index = i
            break
        elif found:
            break

    for line in lines:
        if line.split(" | ")[index] != comp_value:
            #removes line.split(" | ")[index] from line
            line = line.replace(line.split(" | ")[index] + " | ", "")

            print(line, end = "")

def alter(cwd, command):
    #set table name, table contents, and path
    command = helper.removePhrase(command, "alter table ")
    table_name = command.split(' ', 1)[0]

    command = helper.removePhrase(command, table_name + " add ")
    table_contents = " | " + command

    newpath = cwd + "/" + table_name

    #check if table exists
    #if not, modify the table
    if(os.path.exists(newpath)):
        with open(newpath, 'a') as f:
            print("Table " + table_name + " modified.")
            f.write(table_contents)
    else:
        print(helper.bcolors.RED + "!Failed to query " + table_name + " because it does not exist." + helper.bcolors.END)

def insert(cwd, command):
    #remove "insert into " from phrase
    command = helper.removePhrase(command, "insert into ")
    table_name = command.split(' ', 1)[0]
    table_contents = command

    #ensures table exists
    newpath = cwd + "/" + table_name
    if not os.path.exists(newpath) :
        print(helper.bcolors.RED + "!Failed to insert into " + table_name + " because it does not exist." + helper.bcolors.END)
        return

    #remove table name, values, and parenthesis
    #replace commas with pipes
    table_contents = helper.removePhrase(table_contents, table_name + " values")
    if(table_contents[0] == '(' and table_contents[-1] == ')'):
        table_contents = table_contents[1:-1]
    table_contents = table_contents.replace("\'", '')
    table_contents = table_contents.replace("\t", '')
    table_contents = table_contents.replace(' ', '')
    table_contents = table_contents.replace(",", " | ")
    table_contents = table_contents.replace(">", '')

    #open table file for appending
    newpath = cwd + "/" + table_name

    if(os.path.exists(newpath)):
        print("1 new record inserted.")
        with open(newpath, 'a') as f:
            f.write("\n" + table_contents)
    else:
        print(helper.bcolors.RED + "!Failed to insert record into " + table_name + " because it does not exist." + helper.bcolors.END)
    
def update(cwd, command):
    #remove "update " from phrase and set table name
    command = helper.removePhrase(command, "update ")
    table_name = command.split(' ', 1)[0]

    #ensures table exists
    newpath = cwd + "/" + table_name
    if not os.path.exists(newpath):
        print(helper.bcolors.RED + "!Failed to update " + table_name + " because it does not exist." + helper.bcolors.END)
        return

    #remove table name and initialize the selected column for setting
    command = helper.removePhrase(command, table_name + " set ")
    selected_column_set = command.split(' ', 1)[0]

    #open table file for reading, find index of selected column
    with open(table_name, 'r') as f:
        columns = f.readline().strip().split(" | ")
    
    #removes second word from each entry in columns array
    #this is to remove the data type from the column name
    for i in range(len(columns)):
        columns[i] = columns[i].split(' ', 1)[0]

    #find index of selected column for setting
    index_set = 0
    found = False
    for i in range(len(columns)):
        if columns[i] == selected_column_set and not found:
            found = True
            index_set = i
            break
        elif found:
            break
    
    #remove selected column and set phrase from command
    command = command.replace(selected_column_set, '', 1)
    command = command[3:]
    new_entry = command.split(' ', 1)[0]
    new_entry = new_entry.replace("\'", '')

    #initialize the selected column for where
    command = command.replace("\'", '')
    command = helper.removePhrase(command, new_entry + " where ")

    selected_column_where = command.split(' ', 1)[0]

    #find index of selected column for where
    index_where = 0
    for i in range(len(columns)):
        if(columns[i] == selected_column_where):
            index_where = i

    #remove selected column and where phrase from command
    #initialize the operator
    command = helper.removePhrase(command, selected_column_where + " ")
    operator_str = command.split(' ', 1)[0]

    #remove operator from command
    #initialize the value of old entry to be updated
    command = helper.removePhrase(command, operator_str + " ")
    old_entry = command.split(' ', 1)[0]
    old_entry = old_entry.replace("\'", '')

    #if operator is =, operator == 0
    if(operator_str == "="):
        num_changes = 0
        #finds and replaces the old entry with the new entry
        with open(table_name, 'r') as f:
            lines = f.readlines()
        with open(table_name, 'w') as f:
            for line in lines:
                if(line.split(" | ")[index_where] == old_entry):
                    num_changes += 1
                    line = line.split(" | ")
                    line[index_set] = new_entry
                    line = " | ".join(line)
                    line += "\n"
                f.write(line)

        if(num_changes == 1):
            print("1 record modified.")
        else:
            print(str(num_changes) + " records modified.")

def delete(cwd, command):
    command = helper.removePhrase(command, "delete from ")
    table_name = command.split(' ', 1)[0]

    #ensures table exists
    newpath = cwd + "/" + table_name
    if not os.path.exists(newpath):
        print(helper.bcolors.RED + "!Failed to delete from " + table_name + " because it does not exist." + helper.bcolors.END)
        return

    command = helper.removePhrase(command, table_name + " where ")

    selected_column = command.split(' ', 1)[0]

    #open table file for reading, find index of selected column
    with open(table_name, 'r') as f:
        columns = f.readline().strip().split(" | ")
    
    #removes second word from each entry in columns array
    #this is to remove the data type from the column name
    for i in range(len(columns)):
        columns[i] = columns[i].split(' ', 1)[0]

    index = 0
    found = False
    for i in range(len(columns)):
        if columns[i] == selected_column and not found:
            found = True
            index = i
            break
        elif found:
            break
    
    command = helper.removePhrase(command, selected_column + " ")

    operator = command.split(' ', 1)[0]

    command = helper.removePhrase(command, operator)

    comp_value = command
    comp_value = comp_value.replace("\'", '')
    comp_value = comp_value.replace(" ", '')

    #deletes row where column value matches comp_value
    if operator == "=":
        num_deletes = 0
        
        with open(table_name, 'r') as f:
            lines = f.readlines()

        with open(table_name, 'w') as f:
            for line in lines:
                if(line.split(" | ")[index] == comp_value):
                    num_deletes += 1
                else:
                    f.write(line)

        if(num_deletes == 1):
            print("1 record deleted.")
        else:
            print(str(num_deletes) + " records deleted.")
    
    #deletes row where column value is greater than comp_value
    if operator == ">":
        num_deletes = 0

        with open(table_name, 'r') as f:
            lines = f.readlines()

        with open(table_name, 'w') as f:
            for line in lines:
                line = line.strip()

                if(line.split(" | ")[index].find(".") != -1):
                    if(float(line.split(" | ")[index]) > float(comp_value)):
                        num_deletes += 1
                    else:
                        f.write(line + "\n")
                else:
                    f.write(line + "\n")

        if(num_deletes == 1):
            print("1 record deleted.")
        else:
            print(str(num_deletes) + " records deleted.")