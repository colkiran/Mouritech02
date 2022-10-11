
import sqlite3

conn = sqlite3.connect("players.sqlite3")

cursor= conn.cursor()

query = """
create table player (
plyid INTEGER PRIMARY KEY AUTOINCREMENT ,
plyname varchar(50) not null,
sport varchar(50) not null,
acheivement varchar(50) not null
)
"""

cursor.execute(query)

conn.cursor()