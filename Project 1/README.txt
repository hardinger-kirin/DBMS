Kirin Hardinger
CS 457 Fall 2022 - Project 1
Created September 19 2022
Submitted October 6 2022
Resubmitted October 9 2022

How to execute
------------------------------------------------------
Requires python 3
In a UNIX terminal, run "python3 main.py" or run a script as "python3 main.py <PA1_test.sql"
An SQL script can also be run during runtime, such as the command "PA1_test.sql;"

How multiple databases are organized
------------------------------------------------------
Multiple databases are organized as directories using the os library to run system commands.

How multiple tables are organized
------------------------------------------------------
Multiple tables are organized as files within directories using the os library to run system commands.

How required functionalities are implemented
------------------------------------------------------
    CREATE
    ********************
        CREATE DATABASE <db_name> or CREATE TABLE <table_name>
        - Creates a directory with the name <db_name> or file with the name <table_name
        - If the directory/table already exists, it will not be created and an error will be displayed
        - Otherwise, the directory/table will be created and a success message will be displayed

    DROP
    ********************
        DROP DATABASE <db_name> or DROP TABLE <table_name>
        - Deletes a directory with the name <db_name> or file with the name <table_name>
        - If the directory/table does not exist, it will not be deleted and an error will be displayed
        - Otherwise, the directory/table will be deleted and a success message will be displayed

    USE
    ********************
        USE <db_name>
        - Changes the current database/working directory to <db_name>
        - If the database does not exist, it will not be changed and an error will be displayed
        - Otherwise, the current database will be changed and a success message will be displayed

    SELECT
    ********************
        SELECT * FROM <table_name>
        - Displays all the contents of the table <table_name>
        - If the table does not exist, an error will be displayed
        - Otherwise, the contents of the table will be displayed and a success message will be displayed

    ALTER
    ********************
        ALTER TABLE <table_name> <table_contents>
        - Appends new contents to the table <table_name>
        - If the table does not exist, an error will be displayed
        - Otherwise, the content will be appended to the file and a success message will be displayed

    .EXIT
    ********************
        .EXIT
        - Exits the program and displays an "All done." message
