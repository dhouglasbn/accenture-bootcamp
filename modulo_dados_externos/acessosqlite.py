import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute("""
SELECT * FROM users;
""")

data = cursor.fetchall()

print(data)

connection.commit()