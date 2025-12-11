from animal import Animal
class Gato(Animal):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def hacer_sonido(self):
        print('Miau')