#Kirin Hardinger
#CS 457 Fall 2022
#Project 4
#table.py

""" HISTORY

December 2:
    Created beginTransaction function

December 5:
    Finished beginTransaction and commitTransaction functions
    Updated color-coded messages

"""

import helper
import os

#current working table
transaction = False
commit = False

#create table
def createTable(command):
    #initializes command, table name, and path
    command, table_name, newpath = helper.initialize(command, "create table ")

    #separate table contents and replace commas, remove extra ()s
    table_contents = command.replace(",", " |")

    #remove preceding whitespace
    table_contents = table_contents.lstrip()

    if(table_contents[0] == '(' and table_contents[-1] == ')'):
        table_contents = table_contents[1:-1]

    #attempts to create file
    if(not os.path.exists(newpath)):
        with open(table_name, 'w') as f:
            f.write(table_contents)
        print(helper.bcolors.GREEN + "Table " + table_name + " created." + helper.bcolors.END)
    else:
        print(helper.bcolors.RED + "!Failed to create table " + table_name + " because it already exists." + helper.bcolors.END)

    global cwt
    cwt = table_name

#delete table
def dropTable(cwd, command):
    #initializes command, table name, and path
    command, table_name, newpath = helper.initialize(command, "drop table ")

    #check if table exists
    #if so, delete the file
    if(os.path.exists(newpath)):
        os.remove(newpath)
        print("Table " + table_name + " deleted.")
    else:
        print(helper.bcolors.RED + "!Failed to delete table " + table_name + " because it does not exist." + helper.bcolors.END)

#displays all values in table
def selectAll(cwd, command):
    #initializes command, table name, and path
    command, table_name, newpath = helper.initialize(command, "select * from ")

    #attempt to display all table contents
    if(os.path.exists(newpath)):
        with open(newpath, 'r') as f:
            print(f.read())
    else:
        print(helper.bcolors.RED + "!Failed to query table " + table_name + " because it does not exist." + helper.bcolors.END)
    
    global cwt
    cwt = table_name
    
#displays values between two tables given specified column attributes
def selectAllWhere(cwd, command):
    #set table name 1
    command = helper.removePhrase(command, "select * from ")
    table_name_1 = command.split(' ', 1)[0]
    command = helper.removePhrase(command, table_name_1 + " ")

    #set reference to table 1
    reference_1 = command.split(' ', 1)[0]
    reference_1 = reference_1.replace(",", '')
    command = helper.removePhrase(command, reference_1 + ", ")

    #set table name 2
    table_name_2 = command.split(' ', 1)[0]
    command = helper.removePhrase(command, table_name_2 + " ")

    #set reference to table 2
    reference_2 = command.split(' ', 1)[0]
    reference_2 = reference_2.replace(",", ' ')
    command = helper.removePhrase(command, reference_2 + " ")

    command = helper.removePhrase(command, "where ")

    #set table 1 column
    col_1 = command.split(' ', 1)[0]
    col_1 = col_1.replace(reference_1 + ".", '')
    command = helper.removePhrase(command, reference_1 + "." + col_1 + " ")

    #set operator
    operator = command.split(' ', 1)[0]
    command = helper.removePhrase(command, operator + " ")

    #set table 2 column
    col_2 = command.split(' ', 1)[0]
    col_2 = col_2.replace(reference_2 + ".", '')
    command = helper.removePhrase(command, reference_2 + "." + col_2 + " ")

    #set paths to tables
    path_1 = cwd + "/" + table_name_1
    path_2 = cwd + "/" + table_name_2

    #load table contents from table 1
    if(os.path.exists(path_1)):
        with open(path_1, 'r') as f:
            content_1 = f.readlines()
    else:
        print(helper.bcolors.RED + "!Failed to select from " + table_name_1 + " because table does not exist." + helper.bcolors.END)

    #load table contents from table 2
    if(os.path.exists(path_2)):
        with open(path_2, 'r') as f:
            content_2 = f.readlines()
    else:
        print(helper.bcolors.RED + "!Failed to select from " + table_name_2 + " because table does not exist." + helper.bcolors.END)
    
    #finds index of col_1 in table 1 and col_2 in table 2
    index_1 = content_1[0].split().index(col_1)
    index_2 = content_2[0].split().index(col_2)

    print("")

    #searches through table 1 and table 2 for matching values
    first_pass = True
    for line_1 in content_1:
        for line_2 in content_2:
            #prints out table headers
            if first_pass:
                print(line_1.strip() + " | " + line_2.strip())
                first_pass = False

            #prints line_1 and line_2 if line_1[index_1] == line_2[index_2]
            else:
                if(line_1.split()[index_1] == line_2.split()[index_2]):
                    print(line_1.strip() + " | " + line_2.strip())

#displays values between two tables given specified join on column attributes
def selectAllJoin(cwd, command):
    #set table name 1
    command = helper.removePhrase(command, "select * from ")
    table_name_1 = command.split(' ', 1)[0]
    command = helper.removePhrase(command, table_name_1 + " ")

    #set reference to table 1
    reference_1 = command.split(' ', 1)[0]
    reference_1 = reference_1.replace(",", '')
    command = helper.removePhrase(command, reference_1 + " ")

    #set join type
    join = command.split("join", 1)[0]
    command = helper.removePhrase(command, join + "join ")

    #set table name 2
    table_name_2 = command.split(' ', 1)[0]
    command = helper.removePhrase(command, table_name_2 + " ")

    #set reference to table 2
    reference_2 = command.split(' ', 1)[0]
    command = helper.removePhrase(command, reference_2 + " on ")

    #set table 1 column
    col_1 = command.split(' ', 1)[0]
    col_1 = col_1.replace(reference_1 + ".", '')
    command = helper.removePhrase(command, reference_1 + "." + col_1 + " ")

    #set operator
    operator = command.split(' ', 1)[0]
    command = helper.removePhrase(command, operator + " ")

    #set table 2 column
    col_2 = command.split(' ', 1)[0]
    col_2 = col_2.replace(reference_2 + ".", '')
    command = helper.removePhrase(command, reference_2 + "." + col_2 + " ")

    #set paths to tables
    path_1 = cwd + "/" + table_name_1
    path_2 = cwd + "/" + table_name_2

    #load table contents from table 1
    if(os.path.exists(path_1)):
        with open(path_1, 'r') as f:
            content_1 = f.readlines()
    else:
        print(helper.bcolors.RED + "!Failed to select from " + table_name_1 + " because table does not exist." + helper.bcolors.END)

    #load table contents from table 2
    if(os.path.exists(path_2)):
        with open(path_2, 'r') as f:
            content_2 = f.readlines()
    else:
        print(helper.bcolors.RED + "!Failed to select from " + table_name_2 + " because table does not exist." + helper.bcolors.END)

    #finds index of col_1 in table 1 and col_2 in table 2
    index_1 = content_1[0].split().index(col_1)
    index_2 = content_2[0].split().index(col_2)

    print("")

    #if join is inner, search through table 1 and table 2 for matching values
    if "inner" in join:
        first_pass = True
        
        for line_1 in content_1:
            for line_2 in content_2:
                #prints out table headers
                if first_pass:
                    print(line_1.strip() + " | " + line_2.strip())
                    first_pass = False

                #prints line_1 and line_2 if line_1[index_1] == line_2[index_2]
                else:
                    if(line_1.split()[index_1] == line_2.split()[index_2]):
                        print(line_1.strip() + " | " + line_2.strip())
    #otherwise if join is left outer, search through table 1 and table 2 for matching values and fill blank for table 2 unmatched values
    elif "left outer" in join:
        #creates a list of values from content_2 at index_2
        values_2 = []
        for line_2 in content_2:
            values_2.append(line_2.split()[index_2])

        first_pass = True
        
        #searches through table 1 and table 2
        for line_1 in content_1:
            for line_2 in content_2:
                #prints out table headers
                if first_pass:
                    print(line_1.strip() + " | " + line_2.strip())
                    first_pass = False
                    break
                #prints line_1 and line_2 if line_1[index_1] == line_2[index_2]
                elif(line_1.split()[index_1] == line_2.split()[index_2]):
                    print(line_1.strip() + " | " + line_2.strip())
                    continue
            #only prints line_1 if line_1.split(index_1) has not shown up before
            else:
                if line_1.split()[index_1] not in values_2:
                    #displays line_1 with blank values for table 2 including delimeter | for every missing column
                    print(line_1.strip() + " | " + " | " * (len(content_2[0].split()) - 4))
    
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

    global cwt
    cwt = table_name

#appends new column value to table
def alter(cwd, command):
    #initializes command, table name, and path
    command, table_name, newpath = helper.initialize(command, "alter table ")

    command = helper.removePhrase(command, "add ")
    table_contents = " | " + command

    #attempt to append column to table
    if(os.path.exists(newpath)):
        with open(newpath, 'a') as f:
            print("Table " + table_name + " modified.")
            f.write(table_contents)
    else:
        print(helper.bcolors.RED + "!Failed to alter " + table_name + " because it does not exist." + helper.bcolors.END)

    global cwt
    cwt = table_name

#appends new row to table
def insert(cwd, command):
    #initializes command, table name, and path
    command, table_name, newpath = helper.initialize(command, "insert into ")
    table_contents = command

    #ensures table exists
    if not os.path.exists(newpath) :
        print(helper.bcolors.RED + "!Failed to insert into " + table_name + " because it does not exist." + helper.bcolors.END)
        return

    #remove table name, values, and parenthesis
    #replace commas with pipes
    table_contents = helper.removePhrase(table_contents, "values ")

    #removes ( and ) in table_contents
    table_contents = table_contents.replace("(", '')
    table_contents = table_contents.replace(")", '')
    table_contents = table_contents.replace("\'", '')
    table_contents = table_contents.replace("\t", '')
    table_contents = table_contents.replace(' ', '')
    table_contents = table_contents.replace(",", " | ")
    table_contents = table_contents.replace(">", '')

    #finds '--' in table_contents and removes everything after it
    if "--" in table_contents:
        table_contents = table_contents.split("--", 1)[0]

    print(helper.bcolors.GREEN + "1 new record inserted." + helper.bcolors.END)
    with open(newpath, 'a') as f:
        f.write("\n" + table_contents)

    global cwt
    cwt = table_name
    
def update(cwd, command):  
    orig_command = command

    #initializes command, table name, and path
    #remove "update " from phrase and set table name
    command = helper.removePhrase(command, "update ")
    table_name = command.split(' ', 1)[0]

    #check if transaction is in progress
    global transaction
    if transaction is False:
        print(helper.bcolors.RED + "!Failed to update because there is no transaction in progress." + helper.bcolors.END)
        return

    #check if table exists
    newpath = cwd + "/" + table_name
    if not os.path.exists(newpath):
        print(helper.bcolors.RED + "!Failed to update " + table_name + " because it does not exist." + helper.bcolors.END)
        return

    #check if table is already locked
    global commit
    if os.path.exists(newpath + "_lock") and not commit:
        print(helper.bcolors.RED + "Error: Table " + table_name + " is locked!" + helper.bcolors.END)
        transaction = False
        return

    #create lock file and put command in it
    with open(newpath + "_lock", 'w') as f:
        f.write(orig_command)

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

                    if commit is True:
                        line = line.split(" | ")
                        line[index_set] = new_entry
                        line = " | ".join(line)
                        line += "\n"
                f.write(line)

        if(num_changes == 1):
            if not commit:
                print(helper.bcolors.GREEN + "1 record modified." + helper.bcolors.END)
        else:
            if not commit:
                print(helper.bcolors.GREEN + str(num_changes) + " records modified." + helper.bcolors.END)

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

def beginTransaction():
    global transaction
    transaction = True
    print(helper.bcolors.GREEN + "Transaction starts." + helper.bcolors.END)

def commitTransaction(cwd):
    global transaction

    if transaction is False:
        print(helper.bcolors.RED + "Transaction abort." + helper.bcolors.END)
        return

    global commit
    commit = True
    print(helper.bcolors.GREEN + "Transaction committed." + helper.bcolors.END)

    #open any files with _lock in the name, run the commands in the file
    for file in os.listdir("."):
        if file.endswith("_lock"):
            with open(file, 'r') as f:
                lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    helper.commandHandler(cwd, line)
            os.remove(file)

    commit = False
    transaction = False