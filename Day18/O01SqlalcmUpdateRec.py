import sqlalchemy
from sqlalchemy import create_engine, text, MetaData, Column, String, update
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine("sqlite:///players.sqlite3")
metadata = MetaData(bind=engine)

class Player(Base):

    __tablename__ = 'Player'

    playerid = Column(String, primary_key=True)
    plyname = Column(String)
    sport = Column(String)
    achvmnt = Column(String)

connection = engine.connect()
updQry = update(Player)
updQry = updQry.values({'plyname': 'Sachin Ramesh Tendulkar'})
updQry = updQry.where(Player.playerid == 'PLY001')
connection.execute(updQry)

# Fetch the updated data from the database
Player = sqlalchemy.Table('Player', metadata, autoload = True, autoload_with = engine)
query = sqlalchemy.select([Player])

result = connection.execute(query)
print(Player.columns.keys())

for rec in result.fetchall():
    print(rec)
