import pickle

fichero = open("lista_nombres", "rb") # leer binario

lista = pickle.load(fichero)

print(lista)