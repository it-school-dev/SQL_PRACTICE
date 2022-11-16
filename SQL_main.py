import sqlite3
import json

def execute_query(connect, query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        con.commit()
        print('Executed query')
    except Exception as ex: 
        print('Error: \n', str(ex))

def execute_many_querry(connect, query, data):
    cursor = connect.cursor()
    try:
        cursor.executemany(query, data)
        con.commit()
        print('Executed query')
    except Exception as ex: 
        print('Error: \n', str(ex))

with open('parsed_data.json',encoding = 'utf-8') as stream:
    data = json.load(stream)
    print(data)



con = sqlite3.connect('wildberries_data.db')

query = 'INSERT INTO data VALUES (?, ?, ?)'
create = 'CREATE TABLE data(name VARCHAR(60), price NUMERIC(60), link VARCHAR(150))'

execute_query(con, create)

execute_many_querry(con, query, ('2', '1', '1'))



for d in data:
    execute_many_querry(con, query ,[tuple(d.values())])

con.close()

cursor = con.cursor()
cursor.execute('CREATE TABLE data(name VARCHAR(60), price NUMERIC(6,0), link VARCHAR(150))')

con = sqlite3.connect('wildberries_data.db')
cursor = con.cursor()
cursor.executemany("INSERT INTO data VALUES (?, ?, ?)", [tuple(data[1].values())])
con.commit()
con.close()






new_con = sqlite3.connect('wildberries_data_0.db')
cursor = new_con.cursor()
res = cursor.execute('SELECT * FROM data')
res.fetchall()[0:]
new_con.close()



res = cursor.execute("SELECT * FROM very_wild_data")

int(list(data[1].values())[1].replace(' ', ''))