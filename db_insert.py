import sqlite3
import json

with sqlite3.connect('bin') as db:
    cursor = db.cursor()
    f = open("vvv.json", encoding='utf-16')
    g = json.load(f)

    for i in g:
        cursor.execute("INSERT INTO test VALUES ('{}', '{}', '{}')".format(*i.values()))
