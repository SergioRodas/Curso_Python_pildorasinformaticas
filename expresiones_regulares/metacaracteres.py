import re

lista_nombres = ['Ana Gómez', 'María Martín', 'Sandra López', 'Santiago Martín', 'Sandra Fernández']

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):
        print(elemento)

print()

for elemento in lista_nombres:
    if re.findall('Martín$', elemento):
        print(elemento)

print()

lista_enlaces = ['http://pildorasinformaticas.es', 'ftp://pildorasinformaticas.es', 'http://pildorasinformaticas.com', 'ftp://pildorasinformaticas.com', 'http://informaticaespaña.com']

for elemento in lista_enlaces:
    if re.findall('es$', elemento):
        print(elemento)

print()

for elemento in lista_enlaces:
    if re.findall('^ftp', elemento):
        print(elemento)

print()

for elemento in lista_enlaces:
    if re.findall('[ñ]', elemento):
        print(elemento)

print()

lista_personas = ['hombres', 'mujeres', 'niños', 'niñas']

for elemento in lista_personas:
    if re.findall('niñ[oa]s', elemento):
        print(elemento)

print()

lista_palabras = ['casa', 'mascota', 'camión', 'camion']

for elemento in lista_palabras:
    if re.findall('cami[óo]n', elemento):
        print(elemento)