import re

nombre_1 = "Sergio Rodas"

nombre_2 = "sergio Ramos"

nombre_3 = "Lionel Messi"

nombre_4 = "Leonel Messi"

cadena_1 = "456456456"

cadena_2 = "a456456456"

codigo_1 = "akdsljadlajdkldsaa71asjdak"

codigo_2 = "akds71ljadlajdkldsaa1asjdak"

codigo_3 = "akdsljadla jdkldsaaasjdak"

if re.match("Sergio", nombre_2, re.IGNORECASE):     #IGNORECASE hace que la búsqueda no distinga entre minúsculas y mayúsculas.
    print("Hemos encontrado el nombre Sergio")
else:
    print("No hemos encontrado el nombre Sergio")

print()

if re.match("L.onel", nombre_4):     # El punto reemplaza cualquier caracter en esa posición
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

print()

if re.match("\d", cadena_1):     # Busca un dígito al comienzo de la cadena
    print("Hemos encontrado el número")
else:
    print("No hemos encontrado el número")

print()

if re.search("Sergio", nombre_2, re.IGNORECASE):     # Busca el parámetro en cualquier punto de la cadena
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

print()

if re.search("71", codigo_3): 
    print("Hemos encontrado el 71")
else:
    print("No hemos encontrado el 71")