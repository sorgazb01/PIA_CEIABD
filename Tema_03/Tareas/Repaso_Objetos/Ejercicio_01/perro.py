class Perro:
    
    # Creamos el constructor de la clase con sus atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Creamos los metodos para dar valor y modificar un atributo
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
    
    # Metodo de la clase
    def saludar(self):
        return 'Hola, soy un perro y me llamo ' + self.nombre