import sqlite3

conn = sqlite3.connect("data.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
              nome TEXT,
              idade INTEGER
              )
""")

conn.commit()

print("Tabela criada com sucesso")

# cursor.execute(
#   "INSERT INTO usuarios VALUES (?,?)",
#   ("Ana", 25)
# )

# conn.commit()
# print("Usuário inserido no banco de dados")

cursor.execute("SELECT * FROM usuarios")

data = cursor.fetchall()

print("Usuários no banco: ")

for user in data:
  print(user)