import sqlite3

conn = sqlite3.connect('result.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts
''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER) 
''')

name = input("Enter file:")
try: 
    handle = open(name)
except:
    print(f'cannot open file: {name}')

i = 0
for line in handle:
    if not line.startswith('From '): continue
    org = line.rstrip().split()[1].split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''
        INSERT INTO Counts (org, count) VALUES (?, 1)
        ''', (org,))
    else:
        cur.execute('''
        UPDATE Counts SET count = count + 1 WHERE org = ?
        ''', (org,))
    conn.commit()
