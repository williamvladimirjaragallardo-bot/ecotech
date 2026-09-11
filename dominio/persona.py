class Persona:
    """Representa una persona en EcoTech."""

    def __init__(self, rut, nombre):
        """Inicializa una persona con su RUT y nombre."""
        self.rut = rut
        self.nombre = nombre

    def __str__(self):
        """Devuelve una representación legible del objeto Persona."""
        return f"Persona: {self.nombre} ({self.rut})"
