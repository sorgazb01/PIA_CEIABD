from vehiculo import Vehiculo

class Coche(Vehiculo):
    
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas
    
    @property
    def puertas(self):
        return self._puertas
    
    @puertas.setter
    def puertas(self, puertas):
        self._puertas = puertas