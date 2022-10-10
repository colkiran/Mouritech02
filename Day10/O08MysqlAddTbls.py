
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="Players", port=3306)

cursor= conn.cursor()

query = """
create table player (
plyid int not null AUTO_INCREMENT PRIMARY KEY,
plyname varchar(50) not null,
sport varchar(50) not null,
acheivement varchar(50) not null
)
"""

cursor.execute(query)

conn.cursor()