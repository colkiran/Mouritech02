
import sqlalchemy as db
from prettytable import PrettyTable

engine = db.create_engine("sqlite:///players.sqlite3")
connection = engine.connect()
metadata = db.MetaData()
Player = db.Table("Player", metadata, autoload=True, autoload_with=engine)

query = db.select([Player])
result = connection.execute(query)

ptbl =  PrettyTable(Player.columns.keys())

for rec in result.fetchall():
   ptbl.add_row(rec)

print(ptbl)
