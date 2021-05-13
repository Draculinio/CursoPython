from vehiculos import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, patente, color, velocidad_maxima,puertas):
        Vehiculo.__init__(self,marca,modelo,patente,color,velocidad_maxima)
        self.puertas = puertas
