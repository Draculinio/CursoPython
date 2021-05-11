class Vehiculo:
    def __init__(self, marca, modelo, patente, color, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.color = color
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def mostrar_informacion(self):
        return ('Este auto es un '+self.marca+' '+self.modelo+' y esta andando a '+str(self.velocidad_actual))

    def acelerar(self,velocidad):
        if self.encendido:
            if type(velocidad) is float:
                raise Exception('Only Integers')
            try:
                velocidad_final = self.velocidad_actual + velocidad
                if velocidad_final< self.velocidad_maxima:
                    self.velocidad_actual = velocidad_final
                else:
                    self.velocidad_actual = self.velocidad_maxima
            except TypeError:
                print('No puedo acelerar eso')
            except ValueError:
                print('Lo que nos pasó no es un integer')
            except:
                print('Excepción atrapada')
            finally:
                print('Se intentó acelerar con '+str(velocidad))
        else:
            print('Debe encender el auto')

    def frenar(self):
        if self.encendido:
            try:
                velocidad_final = self.velocidad_actual - velocidad
                if velocidad_final> 0:
                    self.velocidad_actual = velocidad_final
                else:
                    self.velocidad_actual = self.velocidad_maxima
            except TypeError:
                print('No puedo frenar eso')
            except ValueError:
                print('Lo que nos pasó no es un integer')
            except:
                print('Excepción atrapada')
            finally:
                print('Se intentó frenar con '+str(velocidad))
        else:
            print('Debe encender el auto')

    def encender(self):
        if not self.encendido: #if self.encendido == False
            self.encendido = True
        else:
            print('El auto ya está encendido')

    def apagar(self):
        if self.encendido: #if self.encendido == True
            self.encendido = False
            #self.velocidad_actual = 0
            self.frenar(self.velocidad_actual)
        else:
            print('El auto ya está apagado')

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, patente, color, velocidad_maxima,puertas):
        Vehiculo.__init__(self,marca,modelo,patente,color,velocidad_maxima)
        self.puertas = puertas

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

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color,plegable,estilo):
        super().__init__(marca, modelo, '', color, 0)
        self.plegable = plegable
        self.estilo = estilo
    def encender(self):
        print('Comenzando a pedalear')
    def apagar(self):
        print('Dejando de pedalear')


auto = Automovil('ford', 'fiesta', 'aaa111', 'naranja',160,4)
print(auto.marca)
print(auto.puertas)
camion = Camion('Mercedes Benz','Actros','bbb222','blanco',150,2,5)
print(camion.marca)
print(camion.carga)
camion.cargar(2)
camion.descargar(1)
bici = Bicicleta('Aurora',"a",'verde',True,'Paseo')
bici.encender()
bici.apagar()
