
import sqlite3

conn = sqlite3.connect("ecotech.db")

tablas = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
).fetchall()

for tabla in tablas:
    print(tabla)

conn.close()