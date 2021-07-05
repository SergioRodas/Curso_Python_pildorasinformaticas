def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        # Acciones adicionales que decoran

        print("Vamos a realizar un cálculo:")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo.")

    return funcion_interior

@funcion_decoradora
def suma(num_1, num_2, num3):
    print(num_1 + num_2 + num3)

@funcion_decoradora
def resta(num_1, num_2):
    print(num_1 - num_2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))


suma(7, 5, 8)

print()

resta(12, 10)

print()

potencia(base = 5, exponente = 3)



