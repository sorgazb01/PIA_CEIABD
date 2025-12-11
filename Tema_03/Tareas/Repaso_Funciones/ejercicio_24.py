# 24. Imprimir las primeras N filas de Pascal.
# Crea una función que imprima las primeras N filas del Triángulo de Pascal.
from math import factorial

def mostrarTrianguloPascal(numeroFilas):
    for fila in range(numeroFilas):
        for elemento in range(fila + 1):
            # Para calcular el Triangulo de Pasca se puede hacer con una formula que aplica el factorial,
            # Esta fomula lo que hace es calucular el factorial del nivel del triangulo de pascal en el que
            # nos encontramos 
            # Con el end vamos concatenando cada una de las cadenas
            print(factorial(fila) // (factorial(elemento) * factorial(fila - elemento)), end=' ')
        # Para mostar un salto de linea
        print()

numeroFilas = int(input('Introduce el numero de filas del Triangulo de Pascal: '))
mostrarTrianguloPascal(numeroFilas)