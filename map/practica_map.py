class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)
    

lista_empleados = [
Empleado("Juan", "Director", 20000),
Empleado("Ana", "Presidenta", 28000),
Empleado("Antonio", "Administrativo", 8000),
Empleado("Sara", "Secretaria", 9000),
Empleado("Mario", "Botones", 6000)
]

def calculo_comision(empleado):
    if empleado.salario <= 7000:
        empleado.salario = empleado.salario * 1.03

    return empleado

lista_empleados_comision = map(calculo_comision, lista_empleados)

for empleado in lista_empleados_comision:
    print(empleado)