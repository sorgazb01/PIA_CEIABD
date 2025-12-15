from figura import Figura
import math

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, radio):
        self._radio = radio
    
    def area(self):
        return math.pi * (self.radio ** 2)