from animal import Animal
class Perro(Animal):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def hacer_sonido(self):
        print('Hola soy un perro,guau')