
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="Players", port=3306)

cursor= conn.cursor()

# query = "insert into player values (0, 'Sachin',  'Cricket', '100 centuries')"
# query = "insert into player values (0, 'Mike Tyson',  'Boxing', '85 Knock outs')"
# query = "insert into player values (0, 'Roger Fedrer',  'Tennis', '25 grandslams')"
# query = "insert into player values (0, 'Lionel Messi',  'Football', '3 gloden boot')"
query = "insert into player values (0, 'Hamilton',  'Formula One', 'Seven Championships')"

cursor.execute(query)

conn.commit()

conn.close()