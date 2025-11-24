# Ejercicio 6
# Diseñar una función que calcule el área y el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia 
# y muestre su área y perímetro.
import math

def calcularArea(radio):
    return math.pi * pow(radio, 2)
    
def calcularPerimetro(radio):
    return 2 * math.pi * radio

radio = float(input('Introduce el radio de una circunferencia: '))
print(f'El perímetro es: {calcularPerimetro(radio)}')
print(f'El área es: {calcularArea(radio)}')