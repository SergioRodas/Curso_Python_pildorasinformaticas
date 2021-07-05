import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla."

texto_buscar = "Python"

texto_encontrado = re.search(texto_buscar, cadena)

if re.search(texto_buscar, cadena) is not None:
    print("He encontrado el texto.")
else:
    print("No he encontrado el texto.")


print(texto_encontrado.start()) # Posición donde empieza
print(texto_encontrado.end())   # Posición donde finaliza
print(texto_encontrado.span())  # Tupla con la ubicación del objeto encontrado

print(len(re.findall(texto_buscar, cadena)))