import sqlite3

# connect to db 
conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

# drop tables if they exist
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')

# create tables
cur.execute('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
''')

cur.execute('''
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
''')

cur.execute('''
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
''')

cur.execute('''
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# use tracks.csv as input
fname = input("Enter file name: ")
try: 
    fh = open(fname)
except: 
    print('cannot open file: {}'.format(fname))
    quit()

for line in fh: 
    # split lines of csv into elements
    elements = line.rstrip().split(',')

    # drop invalid lines
    if len(elements) < 7: continue

    # save elements into variables
    name = elements[0]
    artist = elements[1]
    album = elements[2]
    count = elements[3]
    rating = elements[4]
    length = elements[5]
    genre = elements[6]
    
    # insert data into tables 
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist, ))
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)', (artist_id, album))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)', (name, album_id, genre_id, length, rating, count))

conn.commit()