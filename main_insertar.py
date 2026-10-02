from infraestructura.conexion import (
    obtener_conexion,
    ErrorDeConexion
)

try:

    with obtener_conexion() as conn:

        conn.execute(
            """
            INSERT INTO persona
            (rut, nombre)
            VALUES (?, ?)
            """,
            (
                "12345678-9",
                "Ana Rojas"
            )
        )

    print("Inserción correcta")

except ErrorDeConexion as e:
    print(e)