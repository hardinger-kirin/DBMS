#Kirin Hardinger
#CS 457 Fall 2022
#Project 4
#db.py

""" HISTORY

December 5:
    Updated color-coded messages

"""

import os
import helper

#creates database
def createDb(command):
    #initializes command, database name, and path
    command, db_name, newpath = helper.initialize(command, "create database ")

    #check if database already exists
    #if not, create directory with name of database
    if(not os.path.exists(newpath)):
        os.mkdir(newpath)
        print(helper.bcolors.GREEN + "Database " + db_name + " created." + helper.bcolors.END)
    else:
        print(helper.bcolors.RED + "!Failed to create database " + db_name + " because it already exists." + helper.bcolors.END)

#deletes database
def dropDb(command):
    #initializes command, database name, and path
    command, db_name, newpath = helper.initialize(command, "drop database ")

    #check if directory exists
    #if so, delete the directory
    if(os.path.exists(newpath)):
        os.system(f'rm -r {db_name}')
        print("Database " + db_name + " deleted.")
    else:
        print(helper.bcolors.RED + "!Failed to delete database " + db_name + " because it does not exist." + helper.bcolors.END)

#changes working directory to database directory
def use(cwd, command):
    #initializes command, database name, and path
    command, db_name, newpath = helper.initialize(command, "use ")

    #check if directory exists
    #if so, change working directory
    if(os.path.exists(newpath)):
        if cwd != newpath:
            os.chdir(newpath)
        print(helper.bcolors.GREEN + "Using database " + db_name + "." + helper.bcolors.END)
    else:
        print(helper.bcolors.RED + "!Failed to use database " + db_name + " because it does not exist." + helper.bcolors.END)
