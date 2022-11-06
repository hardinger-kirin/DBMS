#Kirin Hardinger
#CS 457 Fall 2022
#Project 2
#helper.py

""" HISTORY

October 10:
    Created helper.py
    Further modularized code, made it cleaner and more efficient

October 24:
    Moved database-related commands to db.py and table-related commands to table.py
    Created insert functionality

October 29:
    Created update functionality
    Created delete from functionality
    Created select functionality with specified columns

HISTORY """

import sys
import os
import table
import db

rootpath = os.getcwd()

#colors error messages, .EXIT "All done" message
class bcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

#returns current working directory
def getCwd():
    return os.getcwd();

#clears out given phrase from source string
def removePhrase(source, phrase):
    result = source.replace(phrase, "")
    return result;

#ignore comments and empty commands
def checkInput(toCheck):
    if(not toCheck or toCheck.find('--') != -1):
        print("")
        return 1
    if(toCheck == ".exit"):
        programDone()
    else:
        return 0

def programDone():
    print(bcolors.GREEN + "All done." + bcolors.END)
    sys.exit()

#executes commands
def commandHandler(cwd, command):
    if("create database" in command):
        db.createDb(cwd, command)
    
    elif("drop database" in command):
        db.dropDb(cwd, command)

    elif("use" in command):
        db.use(rootpath, command)

    elif("create table" in command):
        table.createTable(cwd, command)

    elif("drop table" in command):
        table.dropTable(cwd, command)

    elif("select * from" in command):
        table.selectAll(cwd, command)
    
    elif("select" in command):
        table.select(cwd, command)

    elif("alter table" in command):
        table.alter(cwd, command)

    elif("insert into" in command):
        table.insert(cwd, command)

    elif("update" in command):
        table.update(cwd, command)

    elif("delete from" in command):
        table.delete(cwd, command)
    
    else:
        print(bcolors.RED + "Unknown command. Try again." + bcolors.END)