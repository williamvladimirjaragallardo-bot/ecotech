from infraestructura.conexion import obtener_conexion

try:

    with obtener_conexion() as conn:

        conn.execute("""
        INSERT INTO empleado
        (
            rut,
            fecha_ingreso,
            sueldo_base
        )
        VALUES
        (
            '99999999-9',
            '2025-01-01',
            500000
        )
        """)

except Exception as e:
    print(e)