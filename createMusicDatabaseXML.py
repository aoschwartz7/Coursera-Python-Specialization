import xml.etree.ElementTree as ET
import sqlite3
# make connection to the database stored in file 'trackdb.sqlite' in same directory
# if it doesn't exist, it will be created
conn = sqlite3.connect('trackdb.sqlite')
# calling cursor() is like calling open() when dealing with text files
cur = conn.cursor()

# Make some new tables using executescript()
# DROP TABLE IF EXISTS removes the table mentioned if it exists;
# allows us to run the same program to create the table over and over without error.
# Create the following columns and insert "Track":
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE,
    genre_id  INTEGER
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    genre TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

''')

# open iTunes library exported as XML:
fname = input('Enter file name: ')
if (len(fname)< 1): fname = 'Library.xml'
# example of how this XML data is formatted:
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

# TODO: what do these next 7 lines do?
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None
# use ElementTree to parse XML in file:
stuff = ET.parse(fname)
# use findall() to retrieve Python list of subtrees that represent the "dict"
# structures in the XML tree:
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
# assign k-v pairs listed below for Track ID if Track ID exists:
for entry in all:
    if (lookup(entry, 'Track ID') is None) : continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    # if an entry is incomplete, skip to the next iteration without adding Track
    # ID to database via "continue":
    if name is None or artist is None or album is None or genre is None :
        continue
    print(name, artist, album, genre, count, rating, length)
    # insert entry into table
    # use "OR IGNORE" so we don't add multiple copies of same entry
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    # use SELECT to retrieve row we just inserted into table and generate new
    # artist_id
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    # insert entry into table and attribute artist_id to album
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    # insert entries into Track table once we've created/filled the above tables
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre, genre_id, length, rating, count ) )
        
    #use commit() to force the data to be written to the database
    connect.commit()
