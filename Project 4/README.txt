Kirin Hardinger
CS 457 Fall 2022 - Project 4
Created November 28 2022
Submitted December 5 2022

How to execute
------------------------------------------------------
Requires python 3
In a UNIX terminal, run "python3 main.py"
Enter commands one at a time.

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

How joins are implemented
------------------------------------------------------
Table joins are implemented using nested for loops to iterate through the rows of each table and compare the values of the columns that are being 
joined on. 

In the case of an inner join, if the values are equal, the row is added to the result table.

In the case of a left outer join, the result table is initialized with all the rows of the left table. Then, the nested for loops are used to compare
the values of the columns that are being joined on. If the values are equal, the row is added to the result table. If the values are not equal, the
row is added to the result table with a space " " for the columns that are not in the left table.

How transactions are implemented
------------------------------------------------------
Transactions are implemented using a transaction log/lock file. The transaction log/lock file is a text file that stores the commands that are to be executed 
in a transaction. When a transaction is started, the transaction log file is opened and the commands are written to the file. When a transaction is
committed, the transaction log/lock file is closed and the commands are executed. When a transaction is aborted, the transaction log file is closed and
the commands are not executed.

The update command is only executed if the transaction is started and there is no log/lock file for the table to be updated. If there is a log/lock file,
the update command is not executed and an error message is printed.

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

        SELECT * FROM <table_name_1> <ref_1>, <table_name_2> <ref_2>
        where <ref_1>.<col_1> = <ref_2>.<col_2>
        - Displays all the contents of the tables <table_name_1> and <table_name_2> where <ref_1>.<col_1> = <ref_2>.<col_2>
        - If the tables do not exist, an error will be displayed
        - Otherwise, the contents of the tables will be displayed

        SELECT * FROM <table_name_1> <ref_1> <join type> join <table_name_2> <ref_2>
        on <ref_1>.<col_1> = <ref_2>.<col_2>
        - Displays all the contents of the tables <table_name_1> and <table_name_2> where <ref_1>.<col_1> = <ref_2>.<col_2> based on the specified join
        - If the tables do not exist, an error will be displayed
        - Otherwise, the contents of the tables will be displayed

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
        - Ensures that a transaction has started and there is no lock on the table
        - Updates the contents of the table <table_name> where the condition is met
        - If the table does not exist, an error will be displayed
        - Otherwise, the content will be updated and a success message will be displayed
    
    DELETE
    ********************
        DELETE FROM <table_name> WHERE <condition>
        - Deletes the contents of the table <table_name> where the condition is met
        - If the table does not exist, an error will be displayed
        - Otherwise, the content will be deleted and a success message will be displayed
    
    BEGIN TRANSACTION
    ********************
        BEGIN TRANSACTION
        - Starts a transaction
        - If a transaction has already started, an error will be displayed
        - Otherwise, a success message will be displayed
    
    COMMIT
    ********************
        COMMIT
        - Commits the transaction
        - If a transaction has not started, an error will be displayed
        - Otherwise, a success message will be displayed

    .EXIT
    ********************
        .EXIT
        - Exits the program and displays an "All done." message
