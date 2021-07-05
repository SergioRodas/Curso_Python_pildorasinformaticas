class Coche():

    def __init__(self):

        self.__largo_chasis = 250 # Encapsulamiento `__` para que no se pueda alterar desde fuera.
        self.__ancho_chasis = 120
        self.__ruedas = 4  
        self.__en_marcha = False

    def arrancar(self, arrancamos):
        self.__en_marcha = arrancamos

        if self.__en_marcha:
            chequeo = self.__chequeo_interno()

        if self.__en_marcha and chequeo:
            return "El coche está en marcha."
        elif self.__en_marcha and chequeo == False:
            return "Algo ha ido mal en el chequeo. No podemos arrancar."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__ancho_chasis, "y un largo de", self.__largo_chasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno.")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else: 
            return False
    

        

print("----------A continuación creamos el primer objeto----------")

print()

mi_coche = Coche()

print(mi_coche.arrancar(True))

mi_coche.estado()

print()

print("----------A continuación creamos el segundo objeto----------")

print()

mi_coche_2 = Coche()

print(mi_coche_2.arrancar(False))

mi_coche_2.__ruedas = 2           # No modifica nada porque la propiedad está encapsulada.

mi_coche_2.estado()
