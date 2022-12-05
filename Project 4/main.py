#Kirin Hardinger
#CS 457 Fall 2022
#Project 4
#main.py

""" HISTORY



"""

import helper

#main program loop
while(1):
    cont = False

    #re-initialize u_input every loop
    u_input = ""

    #cwd path
    cwd = helper.getCwd();

    #receive input
    #handle multi-line inputs
    while(u_input.find(";") == -1):
        #receive input and format command line
        u_input += input("   > ").strip().lower()

        #ensure input is valid
        if(helper.checkInput(u_input) == 1):
            cont = True
            break

        #if multi-line input, separate commands with a space
        if ";" not in u_input:
            u_input += " "

        #if .EXIT, exit
        if(u_input.find(".exit") != -1):
            helper.programDone()

        #if running a script
        if(u_input.find('.sql') != -1):
            cont = True
            print(helper.bcolors.RED + "!Please run scripts from the command line as python3 main.py <name_of_script.sql" + helper.bcolors.END)
            break

    #continue to next loop
    if cont:
        continue

    #remove any ; in input and send to commandHandler
    u_input = u_input.replace(';', "")
    helper.commandHandler(cwd, u_input)