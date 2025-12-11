from vehiculo import Vehiculo

class Camion(Vehiculo):
    
    def __init__(self, marca, capacidad):
        super().__init__(marca)
        self.capacidad = capacidad
        
    @property
    def capacidad(self):
        return self._capacidad
    
    @capacidad.setter
    def capacidad(self, capacidad):
        self._capacidad = capacidad