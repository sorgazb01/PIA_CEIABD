# 24. Imprimir las primeras N filas de Pascal.
# Crea una función que imprima las primeras N filas del Triángulo de Pascal.
from math import factorial

def mostrarTrianguloPascal(numeroFilas):
    # Recorremos cada una de las filas del triangulo de pascal
    # que queremos generar
    for fila in range(numeroFilas):
        # Recorremos cada uno de los elementos de la fila
        # cada fila tiene tantos elementos como su numero de fila + 1
        for elemento in range(fila + 1):
            # Para calcular el valor de cada elemento de la fila usamos la formula:
            # C(fila, elemento) = fila! / (elemento! * (fila - elemento)!)
            # con end= ' ' hacemos que no se genere un salto de linea
            print(factorial(fila) // (factorial(elemento) * factorial(fila - elemento)), end=' ')
        # Para mostar un salto de linea cuando hayamos mostrados todos los
        # elementos de la fila
        print()

numeroFilas = int(input('Introduce el numero de filas del Triangulo de Pascal: '))
mostrarTrianguloPascal(numeroFilas)