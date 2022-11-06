#Kirin Hardinger
#CS 457 Fall 2022
#Project 2
#db.py

""" HISTORY

October 24:
    Created db.py
    Took db-related commands from helper.py and put them into db.py

"""

import os
import helper

def createDb(cwd, command):
    #set database name and path
    db_name = helper.removePhrase(command, "create database ")
    newpath = cwd + "/" + db_name

    #check if database already exists
    #if not, create directory with name of database
    if(not os.path.exists(newpath)):
        os.mkdir(newpath)
        print("Database " + db_name + " created.")
    else:
        print(helper.bcolors.RED + "!Failed to create database " + db_name + " because it already exists." + helper.bcolors.END)

def dropDb(cwd, command):
    #set database name and path
    db_name = helper.removePhrase(command, "drop database ")
    newpath = cwd + "/" + db_name

    #check if directory exists
    #if so, delete the directory
    if(os.path.exists(newpath)):
        os.system(f'rm -r {db_name}')
        print("Database " + db_name + " deleted.")
    else:
        print(helper.bcolors.RED + "!Failed to delete database " + db_name + " because it does not exist." + helper.bcolors.END)

def use(rootpath, command):
    #set database name and path
    db_name = helper.removePhrase(command, "use ")
    newpath = rootpath + "/" + db_name

    #check if directory exists
    #if so, change working directory
    if(os.path.exists(newpath)):
        os.chdir(newpath)
        print("Using database " + db_name + ".")
    else:
        print(helper.bcolors.RED + "!Failed to use database " + db_name + " because it does not exist." + helper.bcolors.END)
