from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.registro_tiempo import RegistroTiempo
from dominio.persona import Persona

def main():
    dep = Departamento("Operaciones")
    ana = Empleado("12345678-9", "Ana Rojas", "2024-03-01", 950_000)

    dep.agregar_empleado(ana)

    registro = RegistroTiempo("2024-03-05", 8)
    ana.registrar_hora(registro)

    print(dep)
    print(ana)
    print(f"Horas registradas: {ana.total_horas()}")

if __name__ == "__main__":
    main()
