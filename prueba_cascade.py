from infraestructura.conexion import obtener_conexion

with obtener_conexion() as conn:

    conn.execute(
        "INSERT OR IGNORE INTO persona VALUES (?, ?)",
        ("11111111-1", "Pedro")
    )

    conn.execute(
        """
        INSERT OR IGNORE INTO empleado
        (
            rut,
            fecha_ingreso,
            sueldo_base
        )
        VALUES
        (
            ?,
            ?,
            ?
        )
        """,
        (
            "11111111-1",
            "2025-01-01",
            600000
        )
    )

    conn.execute(
        """
        INSERT INTO registro_tiempo
        (
            empleado_rut,
            proyecto_id,
            horas,
            fecha
        )
        VALUES
        (
            ?,
            ?,
            ?,
            ?
        )
        """,
        (
            "11111111-1",
            1,
            8,
            "2025-01-01"
        )
    )

with obtener_conexion() as conn:

    conn.execute(
        "DELETE FROM empleado WHERE rut=?",
        ("11111111-1",)
    )

with obtener_conexion() as conn:

    filas = conn.execute(
        "SELECT * FROM registro_tiempo"
    ).fetchall()

    print(filas)