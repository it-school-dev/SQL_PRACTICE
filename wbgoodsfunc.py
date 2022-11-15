import sqlite3


def price_more_than(limit):
    
    db = sqlite3.connect(r'C:\Users\79181\Школа IT\selenium intro\wb_goods_database.db')
    cursor = db.cursor()
    cursor.execute(f'''
        SELECT title, price FROM goods
        WHERE goods.price > {limit}
    ''')
    res = cursor.fetchall()

    return res

print(price_more_than(10000))
