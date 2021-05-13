from vehiculos import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, patente, color, velocidad_maxima,puertas,carga):
        Vehiculo.__init__(self,marca,modelo,patente,color,velocidad_maxima)
        self.puertas = puertas
        self.carga = carga
        self.cargaActual = 0
    def cargar(self,tn):
        self.cargaActual = self.cargaActual+tn
    def descargar(self,tn):
        self.cargaActual = self.cargaActual-tn
