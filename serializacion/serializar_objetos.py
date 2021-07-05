from os import read
import pickle

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        
    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo,"\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)

coche_1 = Vehiculo("Mazda", "MX5")
coche_2 = Vehiculo("Seat", "Leon")
coche_3 = Vehiculo("Bmw", "m5")

coches = [coche_1, coche_2, coche_3]

fichero = open("los_coches", "wb") # escritura binaria

pickle.dump(coches, fichero)

fichero.close()

del(fichero)


