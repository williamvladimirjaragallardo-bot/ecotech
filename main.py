from infraestructura.conexion import obtener_conexion


with obtener_conexion() as conn:
    conn.execute(
        "INSERT INTO persona (rut, nombre) VALUES (?, ?)",
        ("12345678-9", "Ana Rojas"),
    )

with obtener_conexion() as conn:
    filas = conn.execute(
        "SELECT rut, nombre FROM persona"
    ).fetchall()

    for fila in filas:
        print(fila)