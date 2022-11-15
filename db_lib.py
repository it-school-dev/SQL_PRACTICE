def change_name(id, name, cursor, db):
    cursor.execute('''
        UPDATE users SET name = ? WHERE id = ?
    ''', (name, id))
    db.commit()
