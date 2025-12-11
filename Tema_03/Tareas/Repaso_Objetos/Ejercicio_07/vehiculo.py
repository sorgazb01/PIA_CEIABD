class Vehiculo:
    
    def __init__(self, marca):
        self.marca = marca
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca