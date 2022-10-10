
import sqlite3

conn = sqlite3.connect("players.sqlite3")

cursor = conn.cursor()

query = "create database players"

cursor.execute(query)

conn.close()
