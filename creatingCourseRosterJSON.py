# this program will create a SQL database of course rosters that list
# Users (by name), Courses, and Members (whether user is student or teacher)
import json
import sqlite3
# make connection to the database stored in file 'rosterdb.sqlite' in same directory
# if it doesn't exist, it will be created
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Create tables for User, Member, and Course
# Member table will link User and Course tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# example of how JSON data is formatted: 'Name', 'Course', 'Role' (1=teacher)
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],
# open JSON file in read mode:
str_data = open(fname).read()
#load string data with JSON format:
json_data = json.loads(str_data)
#store json_data entries according to dictionary index for name, title and role
for entry in json_data:
    name = entry[0];
    title = entry[1];
    role = entry[2];

    print((name, title, role))
    # insert entry into table
    # use "OR IGNORE" so we don't add multiple copies of same entry
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    # use SELECT to retrieve row we just inserted into table and generate new
    # user_id
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]
    # insert entries into Member table once we've created/filled the above tables
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    #use commit() to force the data to be written to the database
    conn.commit()
