
from sqlalchemy import create_engine, MetaData, Table, Column, String

engine = create_engine("sqlite:///players.sqlite3", echo=True)
meta= MetaData()

Player = Table(
    "Player", meta,

    Column('playerid',String, prirmary_key=True),
    Column('plyname',String),
    Column('sport', String),
    Column('achvmnt', String)
)

conn = engine.connect()
qry = Player.delete().where(Player.c.playerid == 'PLY005')
conn.execute(qry)

p = Player.select()
for rec in conn.execute(p).fetchall():
    print(rec)
