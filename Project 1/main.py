#Kirin Hardinger
#CS 457 Fall 2022
#Project 1

""" HISTORY

September 19:
    Created project in C++

September 21:
    Modularized create, drop, and use functions to make main function simpler
    Updated README outline

September 26:
    Program ignores comments (input that includes "--")
    Created functionality for ALTER and SELECT

October 3:
    Completely restarted project in python

October 6:
    Wrote README file and submitted project

October 9:
    Added functionality to run a script during runtime
    Resubmitted assignment

HISTORY """

import sys
import os
rootpath = os.getcwd()

#helper functions
""""""
#Error messages are colored red, "All done" at .EXIT is colored green
class bcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

#clears out given phrase from source string
def removePhrase(source, phrase):
    query = source.replace(phrase, "")
    return query;

#handle .EXIT, ignore comments, empty commands, and ensure command ends with a ;
def checkInput(toCheck):
    if(not toCheck or toCheck.find('--') != -1):
        print("")
        return 1
    if(toCheck == ".EXIT"):
        print(bcolors.GREEN + "All done." + bcolors.END)
        sys.exit()
    if(toCheck.find(';') == -1):
        print(bcolors.RED + "Command must end with ;" + bcolors.END)
        return 1
    
    return 0

#runs a script line-by-line
def scriptRun(script_name):
    #remove ; from command, open file for reading
    script_name = script_name.replace(';', "")
    script = open(script_name, 'r')
    lines = script.readlines()

    #format command and send to commandHandler
    for line in lines:
        line = line.strip()

        if(checkInput(line) == 1):
            continue
        line = line.replace(';', "")

        cwd = os.getcwd()

        commandHandler(cwd, line)
    
    #close script when complete
    script.close()

#executes commands
def commandHandler(cwd, command):
    if("CREATE DATABASE" in command):
        #set database name and path
        db_name = removePhrase(command, "CREATE DATABASE ")
        newpath = cwd + "/" + db_name

        #check if database already exists
        #if not, create directory with name of database
        if(not os.path.exists(newpath)):
            os.mkdir(newpath)
            print("Database " + db_name + " created.")
        else:
            print(bcolors.RED + "!Failed to create database " + db_name + " because it already exists." + bcolors.END)

    elif("CREATE TABLE" in command):
        #separate table name
        command = removePhrase(command, "CREATE TABLE ")
        table_name = command.split()[0]

        #separate table contents and replace commas, remove extra ()s
        command = removePhrase(command, table_name + " ")
        table_contents = command
        table_contents = table_contents.replace(",", " |")
        if(table_contents[0] == '(' and table_contents[-1] == ')'):
            table_contents = table_contents.replace('(', '', 1)
            table_contents = table_contents.replace(')', '', 1)

        #set path and create table if it doesn't already exist
        newpath = cwd + "/" + table_name

        if(not os.path.exists(newpath)):
            with open(table_name, 'w') as f:
                f.write(table_contents)
            print("Table " + table_name + " created.")
        else:
            print(bcolors.RED + "!Failed to create table " + table_name + " because it already exists." + bcolors.END)

    elif("USE" in command):
        #set database name and path
        db_name = removePhrase(command, "USE ")
        newpath = rootpath + "/" + db_name

        #check if directory exists
        #if so, change working directory
        if(os.path.exists(newpath)):
            workingdb = db_name
            os.chdir(newpath)
            print("Using database " + db_name + ".")
        else:
            print(bcolors.RED + "!Failed to use database " + db_name + " because it does not exist." + bcolors.END)

    elif("DROP DATABASE" in command):
        #set database name and path
        db_name = removePhrase(command, "DROP DATABASE ")
        newpath = cwd + "/" + db_name

        #check if directory exists
        #if so, delete the directory
        if(os.path.exists(newpath)):
            os.system(f'rm -r {db_name}')
            print("Database " + db_name + " deleted.")
        else:
            print(bcolors.RED + "!Failed to delete database " + db_name + " because it does not exist." + bcolors.END)

    elif("DROP TABLE" in command):
        #set table name and path
        table_name = removePhrase(command, "DROP TABLE ")
        newpath = cwd + "/" + table_name

        #check if table exists
        #if so, delete the file
        if(os.path.exists(newpath)):
            os.remove(newpath)
            print("Table " + table_name + " deleted.")
        else:
            print(bcolors.RED + "!Failed to delete table " + table_name + " because it does not exist." + bcolors.END)

    elif("SELECT * FROM " in command):
        #set table name and path
        table_name = removePhrase(command, "SELECT * FROM ")
        newpath = cwd + "/" + table_name

        #check if table exists
        #if so, print out all comments
        if(os.path.exists(newpath)):
            with open(newpath, 'r') as f:
                print(f.read())
        else:
            print(bcolors.RED + "!Failed to query table " + table_name + " because it does not exist." + bcolors.END)

    elif("ALTER TABLE " in command):
        #set table name, table contents, and path
        command = removePhrase(command, "ALTER TABLE ")
        table_name = command.split(' ', 1)[0]

        command = removePhrase(command, table_name + " ADD ")
        table_contents = " | " + command

        newpath = cwd + "/" + table_name

        #check if table exists
        #if not, modify the table
        if(os.path.exists(newpath)):
            with open(newpath, 'a') as f:
                print("Table " + table_name + " modified.")
                f.write(table_contents)
        else:
            print(bcolors.RED + "!Failed to query " + table_name + " because it does not exist." + bcolors.END)
    
    else:
        print(bcolors.RED + "Unknown command. Try again." + bcolors.END)

""""""

#main loop
u_input = ""

while(u_input != ".EXIT"):
    #cwd path and working db directory
    cwd = os.getcwd()
    workingdb = ""

    #format command line
    u_input = input("   > ").strip()

    #ensure input is valid
    if(checkInput(u_input) == 1):
        continue
    
    #check if input is attempting to run a script. if so, run script
    if(u_input.find('.sql') != -1):
        scriptRun(u_input)

    #remove any ; in input and send to commandHandler
    u_input = u_input.replace(';', "")
    commandHandler(cwd, u_input)