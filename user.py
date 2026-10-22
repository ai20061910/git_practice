import sqlalchemy 
from sqlalchemy import create_engine, MetaData, ForeignKey, Table, Column, Integer, String, select


connection = engine.connect()

users_values=[ 
{'name':'Masahiro', 'lastname':'Yamamoto'},  
{'name':'Midori', 'lastname' : 'Kawashima'}, 
{'name':'Etsuko','lastname' : 'Kobayashi'},  
{'name':'Ken','lastname' : 'Saito'},  
{'name':'Taro','lastname' : 'Yamada'},  
{'name':'Kentaro','lastname' : 'Suzuki'} 
]

connection.execute(users.insert(), users_values)