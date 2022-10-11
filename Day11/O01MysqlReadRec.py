
import pymysql
from prettytable import from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="players", port=3306)

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

plyTbl = from_db_cursor(cursor)

conn.close()

plyTbl.align['plyname'] = 'l'
plyTbl.align['sport'] = 'l'
plyTbl.align['acheivement'] = 'l'

print(plyTbl)
