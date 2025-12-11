# 33. Crear un programa que imprima la serie de números de un triángulo de Pascal hasta N filas.
# Crea una función que imprima los números en el triángulo de Pascal para N filas.
from math import factorial

def mostrarTrianguloPascal(numeroFilas):
    for fila in range(numeroFilas):
        for elemento in range(fila + 1):
            print(factorial(fila) // (factorial(elemento) * factorial(fila - elemento)))
        print()

numeroFilas = int(input('Introduce el numero de filas del Triangulo de Pascal: '))
mostrarTrianguloPascal(numeroFilas)