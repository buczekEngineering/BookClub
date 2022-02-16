import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

query_create_table_books = "CREATE TABLE IF NOT EXISTS books " \
                     "(id INTEGER PRIMARY KEY," \
                     "title text," \
                     "author text)"

query_create_table_users = "CREATE TABLE IF NOT EXISTS users " \
                           "(id INTEGER PRIMARY KEY," \
                           "username text," \
                           "password text)"

cursor.execute(query_create_table_books)
cursor.execute(query_create_table_users)
connection.commit()
connection.close()