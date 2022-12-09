#Kirin Hardinger
#CS 457 Fall 2022
#Project 5
#helper.py

""" HISTORY

December 5:
    Created select count(*) from <table_name> command
    Created select avg(<column_name>) from <table_name> command
    Created select max(<column_name>) from <table_name> command

"""

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
    return source.replace(phrase, "")

#set name of table or database
def initialize(command, initialPhrase):
    #remove initial phrase from command
    command = removePhrase(command, initialPhrase)

    #set name of table or database
    name = command.split()[0]
    name = name.replace(' ', '')
    if '(' in name:
        name = name.split('(')[0]

    #remove name from command
    command = removePhrase(command, name)

    #set path to table or database
    path = getCwd() + "/" + name

    return command, name, path

#ignore comments and empty commands
def checkInput(toCheck):
    if(not toCheck or (toCheck[0] == '-' and toCheck[1] == '-')):
        print("")
        return 1
    if(toCheck == ".exit"):
        programDone()
    else:
        return 0

#exits program
def programDone():
    print(bcolors.GREEN + "All done." + bcolors.END)
    sys.exit()

#executes commands
def commandHandler(cwd, command):
    if("create database" in command):
        db.createDb(command)
    
    elif("drop database" in command):
        db.dropDb(command)

    elif("use" in command):
        db.use(cwd, command)

    elif("create table" in command):
        table.createTable(command)

    elif("drop table" in command):
        table.dropTable(cwd, command)

    elif("select * from" in command and "where" not in command and "join" not in command):
        table.selectAll(cwd, command)
    
    elif("select * from" in command and "where" in command and "join" not in command):
        table.selectAllWhere(cwd, command)
    
    elif("select * from" in command and "where" not in command and "join" in command):
        table.selectAllJoin(cwd, command)

    elif("select  count(*) from" in command):
        table.selectCount(cwd, command)

    elif("select  avg" in command):
        table.selectAvg(cwd, command)
    
    elif("select  max" in command):
        table.selectMax(cwd, command)
    
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

    elif("begin transaction" in command):
        table.beginTransaction()

    elif("commit" in command):
        table.commitTransaction(cwd)
    
    else:
        print(bcolors.RED + "Unknown command. Try again." + bcolors.END)