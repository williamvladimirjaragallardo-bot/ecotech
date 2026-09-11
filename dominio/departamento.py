class Departamento:
    """Departamento de la empresa que agrupa empleados."""

    def __init__(self, nombre):
        """Inicializa el departamento con su nombre."""
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        """Agrega un empleado al departamento."""
        self.empleados.append(empleado)
        empleado.departamento = self

    def __str__(self):
        """Devuelve una representación legible del departamento."""
        return f"Departamento: {self.nombre} - Empleados: {len(self.empleados)}"
