import sqlite3
import db_lib

# db = sqlite3.connect('test.sqlite3')

# cursor = db.cursor()


## Создание таблицы
# cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             phone TEXT,
#             email TEXT,
#             password TEXT
#         )
# ''')



## Вставка данных


# Единичная вставка
# name = "Anton1"
# phone = "123456"
# email = "anton@email.net"
# password = "GTY45f8"

# cursor.execute('''
#     INSERT INTO users(name, phone, email, password) VALUES(?, ?, ?, ?)
# ''', (name, phone, email, password))
# db.commit()




# Множественная вставка
users = [
    ("u1", "1", "@1", "q1"),
    ("u2", "2", "@2", "q2"),
    ("u3", "3", "@3", "q3")
]

# cursor.executemany('''
#     INSERT INTO users(name, phone, email, password) VALUES(?, ?, ?, ?)
# ''', users)
# db.commit()



## Получение данных

# id = input("enter id: ")

# cursor.execute('''
#     SELECT * FROM users
#     WHERE users.id = ?
# ''', (id))

# user = cursor.fetchall()

# print(user)



## Обновление данных
# id = input("enter id: ")
# name = input("enter name: ")

# cursor.execute('''
#     UPDATE users SET name = ? WHERE id = ?
# ''', (name, id))
# db.commit()



# Удвление таблицы
# cursor.execute('''
#     DROP TABLE IF EXISTS users2
# ''')


# db.close()


## Обработка ошибок и исключений
try:
    db = sqlite3.connect('test.sqlite3')
    cursor = db.cursor()

    db_lib.change_name(1, "Sergey", cursor, db)
    
except Exception as ex:
    db.rollback()
    raise ex
