class Vehiculos():
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

class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada."
        else:
            return "La furgoneta no está cargada."

class Moto(Vehiculos):      # De esta manera declaro su herencia.
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
    
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo,"\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena, "\n", self.hcaballito)

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargar_energia(self):
        self.cargando = True

mi_moto = Moto("Honda", "CBR")

mi_moto.caballito()

mi_moto.estado()

print()

mi_furgoneta = Furgoneta("Renault", "Kangoo")

mi_furgoneta.arrancar()

mi_furgoneta.estado()

print(mi_furgoneta.carga(True))

class BicicletaElectrica(VElectricos, Vehiculos):
    pass

mi_bici = BicicletaElectrica("Orbea", "HC1030")


