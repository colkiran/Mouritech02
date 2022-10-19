"""
engine = create_engine("mysql+pymysql://root@localhost/players", echo=True)
"""
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///players.sqlite3", echo=True)
Base = declarative_base()

class Player(Base):

    __tablename__ = 'Player'

    playerid = Column(String, primary_key = True)
    plyname = Column(String)
    sport = Column(String)
    achvmnt = Column(String)

    def __init__(self, playerid, plyname, sport, achvmnt):
        self.playerid = playerid
        self.plyname = plyname
        self.sport = sport
        self.achvmnt = achvmnt

Base.metadata.create_all(engine)
