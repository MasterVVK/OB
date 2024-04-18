import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL ,
    age INTEGER NOT NULL)
''')
conn.commit()

#cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Алекс", 33))
#cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Вася", 23))
conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
#print(rows)
for i in rows:
    print(i)
conn.close()