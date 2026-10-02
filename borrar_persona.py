from infraestructura.conexion import obtener_conexion

with obtener_conexion() as conn:

    conn.execute(
        "DELETE FROM persona WHERE rut = ?",
        ("12345678-9",)
    )

print("Persona eliminada")