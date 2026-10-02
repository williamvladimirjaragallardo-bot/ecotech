from infraestructura.conexion import (
    obtener_conexion,
    ErrorDeConexion
)

try:

    with obtener_conexion() as conn:

        filas = conn.execute(
            """
            SELECT rut, nombre
            FROM persona
            """
        ).fetchall()

        for fila in filas:
            print(fila)

except ErrorDeConexion as e:
    print(e)
