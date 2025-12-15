from figura import Figura

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def area(self):
        return self.base * self.altura