import pickle

lista_nombres = ["Sergio", "Ana", "Pedro", "María", "Isabel"]

fichero_binario = open("lista_nombres", "wb") # wb = escritura binaria 

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario)