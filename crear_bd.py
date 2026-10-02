from infraestructura.conexion import obtener_conexion

with open(
    "db/01_esquema.sql",
    "r",
    encoding="utf-8"
) as archivo:
    esquema = archivo.read()

with obtener_conexion() as conn:
    conn.executescript(esquema)

print("Base de datos creada correctamente")