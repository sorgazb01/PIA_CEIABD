# 10.Crea una clase Figura con un método area que calcule el área. Luego, crea
# las subclases Círculo y Rectángulo que sobrescriban el método area para
# calcular el área según la fórmula correspondiente.
from circulo import Circulo
from rectangulo import Rectangulo

ciruclo = Circulo(5)
rectangulo = Rectangulo(10, 4)
print(f'El área del circulo es: {ciruclo.area()}')
print(f'El area del rectangulo es: {rectangulo.area()}')