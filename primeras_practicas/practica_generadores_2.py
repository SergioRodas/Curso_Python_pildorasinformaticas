# Generador con For simple:

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas = devuelve_ciudades("Buenos Aires", "Madrid", "Barcelona", "Santiago")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

print()

# Generador con For anidado:

def devuelve_ciudades_letras(*ciudades):
    for elemento in ciudades:
        for sub_elemento in elemento:
            yield sub_elemento

letras_ciudades = devuelve_ciudades_letras("Buenos Aires", "Madrid", "Barcelona", "Santiago")

print(next(letras_ciudades))
print(next(letras_ciudades))

print()

# Generador con `yield from`:

def devuelve_letras_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

letras_ciudades = devuelve_letras_ciudades("Buenos Aires", "Madrid", "Barcelona", "Santiago")

print(next(letras_ciudades))
print(next(letras_ciudades))