# This script contains tutorials of connecting to SQLite database.
# Created By : Shivam Sharma
# Created On : 14th May 2021

import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect
import mysql.connector
from mysql.connector import Error


def create_con(host_name, username, password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
                     host = host_name,
                     user = username,
                     passwd = password,
                     database = db_name
        )
        print('Connection to MySQL DB is successful.')
    except Error as e:
        print(f'The Error is {e}')
    
    return connection

def executer(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Query Executed successfully.')
    except Error as e:
        print(f'Error Encountered : {e}')


connection = create_con('localhost', 'ROOT', 'Active@1925', 'DB_TEST')
# table_q = 'CREATE TABLE USERS(ID INTEGER, NAME TEXT)'
# executer(connection, table_q)
table_insert_q = "INSERT INTO USERS VALUES(13, 'SHARMA')"
executer(connection, table_insert_q)