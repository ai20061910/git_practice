import sqlalchemy 
from sqlalchemy import create_engine, MetaData, ForeignKey, Table, Column, Integer, String, select

meta = MetaData()

users=Table(
    'users', meta,
    Column('id', Integer,primary_key = True),
    Column('name', String),
    Column('lastname', String)
)

address = Table(
    'address',meta,
    Column('id',Integer,primary_key=True),
    Column('user_id',Integer,ForeignKey('users.id')),
    Column('postal_add',String),
    Column('email_add',String)
)
engine = create_engine('sqlite:///core_users.db')
meta.create_all(engine)