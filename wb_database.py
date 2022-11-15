import sqlite3
import json


with open(r'C:\Users\79181\Школа IT\selenium intro\goodswb.json', 'r', encoding='utf-16') as f:
    dblist = json.load(f)


try:
    db = sqlite3.connect(r'C:\Users\79181\Школа IT\selenium intro\wb_goods_database.db')

    cursor = db.cursor()

    # Создание таблицы
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS goods(
                id INTEGER PRIMARY KEY,
                title TEXT,
                price INTEGER,
                link TEXT
            )
    ''')
    
    db.commit()

    for elem in dblist:
        
        cursor.execute('''
            SELECT link FROM goods
            WHERE link = ?
        ''', (elem['link'],))
        db.commit()

        if cursor.fetchone() == None:

            cursor.execute('''
            INSERT INTO goods(title, price, link) VALUES(?, ?, ?)
            ''', (elem['title'], elem['price'], elem['link']))
        
            db.commit()


    db.close()
    print('all done')


except Exception as ex:
    db.rollback()
    raise ex