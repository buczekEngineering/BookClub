import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

query_create_table = "CREATE TABLE IF NOT EXISTS books " \
                     "(id INTEGER PRIMARY KEY," \
                     "title text," \
                     "author text)"
cursor.execute(query_create_table)
connection.commit()
connection.close()