import re

lista_nombres = ['Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia']

for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento):
        print(elemento)

lista_nombres = ['Ma1', 'Ma2', 'Se1', 'Ba1', 'Va1', 'Ma3', 'Ma4', 'Va2']

for elemento in lista_nombres:
    if re.findall('Ma[0-3]', elemento):
        print(elemento)

lista_nombres = ['Ma1', 'Ma2', 'Se1', 'Ba1', 'Va1', 'Ma3', 'Ma4', 'Va2', 'MaA', 'MaB', 'MaC']

for elemento in lista_nombres:
    if re.findall('Ma[0-3A-B]', elemento):
        print(elemento)