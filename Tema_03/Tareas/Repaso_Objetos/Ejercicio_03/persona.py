class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    
    def saludar(self):
        print(f'Hola, soy {self.nombre}')