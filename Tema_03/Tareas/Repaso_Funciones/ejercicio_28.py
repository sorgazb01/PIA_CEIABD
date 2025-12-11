# 28. Crear un programa que muestre los primeros N cuadrados perfectos.
# Escribe una función que imprima los primeros N números que son cuadrados
# perfectos.
from math import sqrt


def esCuadradoPerfecto(numero):
    raiz = sqrt(numero)
    if raiz.is_integer():
        return True
    else:
        return False

def imprimirCuadradosPerfectos(cantidad):
    contador = 0
    numero = 1
    while contador < cantidad:
        if esCuadradoPerfecto(numero):
            print(numero)
            contador += 1
        numero += 1

n = int(input('Introduce la cantidad de cuadrados perfectos que deseas mostrar: '))
imprimirCuadradosPerfectos(n)