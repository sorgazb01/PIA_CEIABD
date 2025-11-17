class Persona():
    
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self,dni):
        self._dni = dni
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    
    @nombre.setter
    def edad(self,edad):
        self._edad = edad
        
    def mostrar(self):
        return self.dni.mostrar() + ' ' + self.nombre + ' ' + self.edad