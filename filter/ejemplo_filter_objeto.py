class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)
    

lista_empleados = [
Empleado("Juan", "Director", 200000),
Empleado("Ana", "Presidenta", 280000),
Empleado("Antonio", "Administrativo", 80000),
Empleado("Sara", "Secretaria", 90000),
Empleado("Mario", "Botones", 60000)
]

salarios_altos = filter(lambda empleado: empleado.salario > 100000, lista_empleados)

for empleado in salarios_altos:
    print(empleado)