class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    def mostrarDescripcion(self):
        print(f'Animal, Nombre: {self.nombre}')