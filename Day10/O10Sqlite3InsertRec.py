
import sqlite3

conn = sqlite3.connect("players.sqlite3")

cursor= conn.cursor()

query = "insert into player values (0, 'Sachin',  'Cricket', '100 centuries')"

cursor.execute(query)

conn.commit()

conn.close()