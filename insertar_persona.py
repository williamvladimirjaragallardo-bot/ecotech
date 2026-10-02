from infraestructura.conexion import obtener_conexion

with obtener_conexion() as conn:

    conn.execute(
        """
        INSERT INTO persona
        (rut, nombre)
        VALUES (?, ?)
        """,
        (
            "98765432-1",
            "Juan Perez"
        )
    )

print("Persona insertada")