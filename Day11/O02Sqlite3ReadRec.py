
import sqlite3
from prettytable import from_db_cursor

conn = sqlite3.connect("players.sqlite3")

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

plyTbl = from_db_cursor(cursor)

conn.close()

plyTbl.align['plyname'] = 'l'
plyTbl.align['sport'] = 'l'
plyTbl.align['acheivement'] = 'l'

print(plyTbl)
