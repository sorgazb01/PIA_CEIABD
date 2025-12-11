# 24. Imprimir las primeras N filas de Pascal.
# Crea una función que imprima las primeras N filas del Triángulo de Pascal.
from math import factorial

def mostrarTrianguloPascal(numeroFilas):
    for fila in range(numeroFilas):
        for elemento in range(fila + 1):
            print(factorial(fila) // (factorial(elemento) * factorial(fila - elemento)), end=' ')
        print()

numeroFilas = int(input('Introduce el numero de filas del Triangulo de Pascal: '))
mostrarTrianguloPascal(numeroFilas)