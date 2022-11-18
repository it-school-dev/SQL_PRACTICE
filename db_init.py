import sqlite3

with sqlite3.connect('bin') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS test(product TEXT, price TEXT, link TEXT)"""
    cursor.execute(query)
