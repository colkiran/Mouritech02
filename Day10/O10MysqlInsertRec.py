
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="Players", port=3306)

cursor= conn.cursor()

query = "insert into player values (0, 'Sachin',  'Cricket', '100 centuries')"

cursor.execute(query)

conn.commit()

conn.close()