import sqlite3 
conn = sqlite3.connect('ecotech.db')
conn.executescript(open('db/01_esquema.sql', encoding='utf-8').read())

print ("ingrese nombre")
nombre = input()
print ("ingrese rut")
rut = input()


conn.execute(f"INSERT INTO `persona` (`rut`, `nombre`) VALUES ('{rut}', '{nombre}')")
print(conn.execute("Select * from persona").fetchall())
conn.commit()
conn.close()