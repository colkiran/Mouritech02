
import sqlite3

conn = sqlite3.connect("players.sqlite3")

cursor= conn.cursor()

# query = "insert into player values (0, 'Sachin',  'Cricket', '100 centuries')"
# query = "insert into player (plyname, sport, acheivement) values ('Mike Tyson',  'Boxing', '85 Knock outs')"
# query = "insert into player  (plyname, sport, acheivement) values ('Roger Fedrer',  'Tennis', '25 grandslams')"
# query = "insert into player  (plyname, sport, acheivement) values ('Lionel Messi',  'Football', '3 gloden boot')"
query = "insert into player  (plyname, sport, acheivement) values ( 'Hamilton',  'Formula One', 'Seven Championships')"

cursor.execute(query)

conn.commit()

conn.close()