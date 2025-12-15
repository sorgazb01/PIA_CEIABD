class Coche:

    # Creamos el contructor de la clase juntos con sus atributos
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
    
    # Creamos los metodos para dar valor y modificar un atributo
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self, anio):
        self._anio = anio

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

    # Metodo de la clase
    def mostrar(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Color: {self.color}'