from vehiculos import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color,plegable,estilo):
        super().__init__(marca, modelo, '', color, 0)
        self.plegable = plegable
        self.estilo = estilo
    def encender(self):
        print('Comenzando a pedalear')
    def apagar(self):
        print('Dejando de pedalear')
