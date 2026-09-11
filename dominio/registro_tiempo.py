class RegistroTiempo:
    """Registro de horas trabajadas por un empleado."""

    def __init__(self, fecha, horas):
        """Inicializa un registro con fecha y cantidad de horas."""
        self.fecha = fecha
        self.horas = horas

    def __str__(self):
        """Devuelve una representación legible del registro."""
        return f"Registro: {self.fecha} - {self.horas} horas"
