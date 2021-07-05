from modulos import funciones_matematicas
class Areas:
    def area_cuadrado(lado):
        """
        Calcula el área de un cuadrado, elevando al cuadrado el lado pasado por parámetro.
        """
        return "El área del cuadrado es: " + str(lado*lado)

    def area_triangulo(base, altura):
        """
        Calcula el área de un triángulo utilizando los parámetros de base y altura dados.
        Cálculo: (base * altura) /2
        """
        return "El área del triángulo es: " + str((base*altura)/2)

print(Areas.area_triangulo(2,7))
print(Areas.area_triangulo.__doc__)
print(Areas.area_cuadrado(2))
print(Areas.area_cuadrado.__doc__)
help(Areas.area_cuadrado)

help(Areas)
help(funciones_matematicas)