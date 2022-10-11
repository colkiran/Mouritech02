

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="players", port=3306)

cursor = conn.cursor()

query = "update player set plyname = 'Sachin Tendulkar' where plyid = 1"

cursor.execute(query)

conn.commit()

conn.close()

