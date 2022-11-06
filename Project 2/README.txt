Kirin Hardinger
CS 457 Fall 2022 - Project 2
Created October 10 2022
Submitted October 30 2022

How to execute
------------------------------------------------------
Requires python 3
In a UNIX terminal, run "python3 main.py" or run a script as "python3 main.py <PA2_test.sql"

How multiple databases are organized
------------------------------------------------------
Multiple databases are organized as directories using the os library to run system commands.

How multiple tables are organized
------------------------------------------------------
Multiple tables are organized as files within directories using the os library to run system commands.

How tuples are stored in the table
------------------------------------------------------
Tuples are stored in the table as pipe delimited strings in the file.
For example, in a table with an ID, name, address, and phone number:
1 | Jane Doe | 1234 Main St | 123-456-7890

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
        - Otherwise, the contents of the table will be displayed

        SELECT <column_name> FROM <table_name>
        - Displays the contents of the column <column_name> in the table <table_name>
        - If the table does not exist, an error will be displayed
        - Otherwise, the contents of the column will be displayed

    ALTER
    ********************
        ALTER TABLE <table_name> <table_contents>
        - Appends new contents to the table <table_name>
        - If the table does not exist, an error will be displayed
        - Otherwise, the content will be appended to the file and a success message will be displayed

    INSERT
    ********************
        INSERT INTO <table_name> VALUES (<table_contents>)
        - Appends new contents to the table <table_name>
        - If the table does not exist, an error will be displayed
        - Otherwise, the content will be appended to the file and a success message will be displayed

    UPDATE
    ********************
        UPDATE <table_name> SET <table_column> = <table_contents> WHERE <condition>
        - Updates the contents of the table <table_name> where the condition is met
        - If the table does not exist, an error will be displayed
        - Otherwise, the content will be updated and a success message will be displayed
    
    DELETE
    ********************
        DELETE FROM <table_name> WHERE <condition>
        - Deletes the contents of the table <table_name> where the condition is met
        - If the table does not exist, an error will be displayed
        - Otherwise, the content will be deleted and a success message will be displayed

    .EXIT
    ********************
        .EXIT
        - Exits the program and displays an "All done." message
