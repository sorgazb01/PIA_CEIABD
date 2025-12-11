class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def saludar(self):
        return 'Hola, soy un perro y me llamo ' + self.nombre