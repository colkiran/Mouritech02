
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///players.sqlite3")
connection = engine.connect()

class Player(Base):

    __tablename__ = 'Player'

    playerid = Column(String, primary_key = True)
    plyname = Column(String)
    sport = Column(String)
    achvmnt = Column(String)

Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Player).with_entities(Player.playerid, Player.plyname, Player.sport, Player.achvmnt).filter(Player.playerid != 'PLY003')

for rec in result:
    print(rec.playerid, rec.plyname, rec.sport, rec.achvmnt)

session.close()
