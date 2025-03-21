import pandas as pd
import sqlite3

# 1️⃣ Ler o CSV
df = pd.read_csv("vendas.csv")

# 2️⃣ Criar/conectar ao banco de dados SQLite
conn = sqlite3.connect("vendas.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Produto TEXT,
    Quantidade INTEGER,
    Preço REAL
)
''')

df.to_sql("vendas", conn, if_exists="append", index=False)

df_consulta = pd.read_sql("SELECT * FROM vendas", conn)
print("Dados no Banco de Dados SQLite:")
print(df_consulta)


conn.close()