<<<<<<< HEAD
import sqlite3 
conn = sqlite3.connect('ecotech.db')
conn.executescript(open('db/01_esquema.sql', encoding='utf-8').read())

print ("ingrese nombre")
nombre = input()
print ("ingrese rut")
rut = input()


conn.execute(f"INSERT INTO `persona` (`rut`, `nombre`) VALUES ('{rut}', '{nombre}')")
print(conn.execute("Select * from persona").fetchall())
conn.commit()
conn.close()
=======
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
>>>>>>> 945e6243afd35489b62797904a3c4ff6d93ba124
