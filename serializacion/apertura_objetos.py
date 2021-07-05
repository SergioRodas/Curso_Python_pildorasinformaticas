import pickle
from serializar_objetos import Vehiculo

fichero_apertura = open("los_coches", "rb") # lectura binaria

mis_coches = pickle.load(fichero_apertura)

fichero_apertura.close()

for c in mis_coches:
    c.estado()
    print()