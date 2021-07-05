def genera_pares(limite):
    num = 1
    mi_lista = []

    while num < limite:
        
        mi_lista.append(num * 2)

        num = num + 1

    return mi_lista
        
print(genera_pares(10))


def genera_pares_generador(limite):

    num = 1

    while num < limite:
    
        yield num * 2

        num = num + 1

devuelve_pares = genera_pares_generador(10)

print(next(devuelve_pares))

print("Aquí podría haber mas código")

print(next(devuelve_pares))

print("Aquí podría haber mas código")

print(next(devuelve_pares))