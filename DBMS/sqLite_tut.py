# THis script have tutorial to connect to sqLite 
# Created By : Shivam Sharma
# Created On : 14th May 2021

import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection to SQLite DB is successfull')
    except Error as e:
        print('Error Encountered - {e}')
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query executed successfully')
    except Error as e:
        print(f'Error Encountered - {e}')

connection = create_connection('Z:\\DataBases\\sqlite_test.sqlite')
#* Above command will create a file 'sqlite_test.sqlite'


#* CREATING TABLES


#* in SQLite we will use cursor.execute() to execute the command.
create_table_query = '''
                     CREATE TABLE IF NOT EXISTS USERS(
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         NAME TEXT NOT NULL,
                         AGE INTEGER,
                         GENDER TEXT, 
                         NATIONALITY TEXT
                     );
'''
execute_query(connection, create_table_query)

create_post_table_q = '''
                       CREATE TABLE IF NOT EXISTS POSTS(
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           TITLE TEXT NOT NULL,
                           DESCRIPTION TEXT NOT NULL,
                           USER_ID INTEGER NOT NULL,
                           FOREIGN KEY(USER_ID) REFERENCES USERS(ID)
                       );
'''
execute_query(connection, create_post_table_q)

create_comments_table_q = '''
                          CREATE TABLE IF NOT EXISTS COMMENTS(
                              ID INTEGER PRIMARY KEY AUTOINCREMENT,
                              TEXT TEXT NOT NULL,
                              USER_ID INTEGER NOT NULL,
                              POST_ID INTEGER NOT NULL,
                              FOREIGN KEY(USER_ID) REFERENCES USERS(ID) FOREIGN KEY(POST_ID) REFERENCES POSTS (ID)
                          );
'''
execute_query(connection, create_comments_table_q)

create_likes_table_q = '''
                        CREATE TABLE IF NOT EXISTS LIKES(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            USER_ID INTEGER NOT NULL,
                            POST_ID INTEGER NOT NULL,
                            FOREIGN KEY (USER_ID) REFERENCES USERS(ID) FOREIGN KEY (POST_ID) REFERENCES POSTS (ID)
                        ); 
'''
execute_query(connection, create_likes_table_q)

#* INSERTING RECORDS

create_users = '''
INSERT INTO 
    USERS (NAME, AGE, GENDER, NATIONALITY)
VALUES
    ('JAMES', 34, 'MALE', 'USA'),
    ('ASHWINI', 21, 'FEMALE', 'AUSTRALIA'),
    ('ASLAM', 45, 'MALE', 'PALESTINE'),
    ('INDICA', 23, 'MALE', 'JAMICA'),
    ('LEILA', 40, 'FEMALE', 'CANADA');
'''
execute_query(connection, create_users)

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""
execute_query(connection, create_posts)  

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""
execute_query(connection, create_comments)

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""
execute_query(connection, create_likes)  



#* Retrieving the records
# we will use .fetchall() method, it returns the tuples
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'Error encountered - {e}')

print_users_q = 'SELECT*FROM USERS'
users = execute_read_query(connection, print_users_q)

for user in users:
    print(user)



#* Join operations
select_users_posts = '''
SELECT 
    USERS.ID,
    USERS.NAME,
    POSTS.DESCRIPTION
FROM 
    POSTS
    INNER JOIN USERS ON USERS.ID = POSTS.USER_ID
'''
users_posts = execute_read_query(connection, select_users_posts)

for user in users_posts:
    print(user)


#* Where operation
select_post_likes = '''
SELECT 
    DESCRIPTION AS POST,
    COUNT(LIKES.ID) AS LIKES
FROM
    LIKES,
    POSTS
WHERE
    POSTS.ID = LIKES.POST_ID
GROUP BY 
    LIKES.POST_ID
'''
post_likes = execute_read_query(connection, select_post_likes)

for post in post_likes:
    print(post)

#* Updataing talbe records

select_post_desc = 'SELECT DESCRIPTION FROM POSTS WHERE ID = 2'
post_description = execute_read_query(connection, select_post_desc)

for desc in post_description:
    print(desc)

update_post_description = '''
UPDATE
    POSTS
SET
    DESCRIPTION = 'THE WEATHER HAS BECOME PLEASENT NOW'
WHERE 
    ID = 2
'''
execute_query(connectionm, update_post_description)


#* DELETING TABLE RECORDS
delete_comment = "DELETE FROM COMMENTS WHERE ID = 5"
execute_query(connection, delete_comment)
