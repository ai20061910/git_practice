import sqlalchemy 
from sqlalchemy import create_engine, MetaData, ForeignKey, Table, Column, Integer, String, select
from tabulate import tabulate

meta = MetaData()

users=Table(
    'users', meta,
    Column('id', Integer,primary_key = True),
    Column('name', String),
    Column('lastname', String)
)

addresses = Table(
    'address',meta,
    Column('id',Integer,primary_key=True),
    Column('user_id',Integer,ForeignKey('users.id')),
    Column('postal_add',String),
    Column('email_add',String)
)

engine = create_engine('sqlite:///core_users.db')
meta.create_all(engine)

users_values=[ 
{'name':'Masahiro', 'lastname':'Yamamoto'},  
{'name':'Midori', 'lastname' : 'Kawashima'}, 
{'name':'Etsuko','lastname' : 'Kobayashi'},  
{'name':'Ken','lastname' : 'Saito'},  
{'name':'Taro','lastname' : 'Yamada'},  
{'name':'Kentaro','lastname' : 'Suzuki'} 
]

with engine.connect() as connection:
    connection.execute(users.insert(), users_values)
    connection.commit()

addr_values = [ 
{'user_id':1, 'postal_add':'Tokyo Minato-ku', 'email_add':'masahiro@gmail.com'}, 
{'user_id':1, 'postal_add':'Nagoya Tempaku-ku', 'email_add':'masahiro@gmail.com'}, 
{'user_id':3, 'postal_add':'Nagoya Mizuho-ku', 'email_add':'etsuko@gmail.com'}, 
{'user_id':5, 'postal_add':'Kyouto Minami-ku', 'email_add':'taro@gmail.com'}, 
{'user_id':2, 'postal_add':'Osaka Kita-ku', 'email_add':'midori@gmail.com'}
] 

connection = engine.connect()
connection.execute(addresses.insert(), addr_values)
connection.commit()

result = connection.execute(select(users))
result2 = connection.execute(select(addresses))
print(tabulate(result, headers=users.columns.keys(), tablefmt='pretty'))
print(tabulate(result2, headers=addresses.columns.keys(), tablefmt='pretty'))