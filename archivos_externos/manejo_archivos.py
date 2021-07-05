from io import open
from typing import TextIO

archivo_texto = open("archivo.txt", "w")

frase = "Estupendo día para estudiar Python. \nEl sábado a la noche se estudia."

archivo_texto.write(frase)

archivo_texto.close()

archivo_texto = open("archivo.txt", "r")

texto = archivo_texto.read()

archivo_texto.close()

print(texto)

archivo_texto = open("archivo.txt", "r")

lineas_texto = archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[0])

archivo_texto = open("archivo.txt", "a") # Modificación

archivo_texto.write("\nSiempre es una buena ocasión para estudiar Python.")

archivo_texto.close()

archivo_texto = open("archivo.txt", "r") # Solo lectura

#print(archivo_texto.read())

archivo_texto.seek(len(archivo_texto.readline()))

print(archivo_texto.read())

archivo_texto.close()

archivo_texto = open("archivo.txt", "r+") # Lectura y escritura

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta línea ha sido incluída desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()



