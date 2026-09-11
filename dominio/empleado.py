class Empleado:
    """Un empleado de EcoTech. Registra su tiempo en proyectos."""

    def __init__(self, rut, nombre, fecha_ingreso, sueldo_base):
        """Inicializa un empleado con sus datos básicos."""
        self.rut = rut
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso
        self.sueldo_base = sueldo_base
        self.registros = []       # cardinalidad 1..* -> lista
        self.departamento = None  # cardinalidad 0..1 -> puede ser None

    def registrar_hora(self, registro):
        """Agrega un registro de horas trabajadas."""
        self.registros.append(registro)

    def total_horas(self):
        """Devuelve el total de horas registradas."""
        return sum(r.horas for r in self.registros)

    def __str__(self):
        """Devuelve una representación legible del empleado."""
        return f"Empleado: {self.nombre} ({self.rut}) - Sueldo base: ${self.sueldo_base}"
