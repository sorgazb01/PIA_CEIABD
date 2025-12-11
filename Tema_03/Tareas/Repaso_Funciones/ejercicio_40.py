# 40. Crear un programa que calcule la suma de los números de una matriz (2D).
# Crea una función que reciba una matriz de números (lista de listas) y devuelva la
# suma de todos sus elementos.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def sumaMatriz(matriz):
    suma = 0
    for fila in matriz:
        for numero in fila:
            suma += numero
    return suma

print(f'La suma de los elementos de la matriz es: {sumaMatriz(matriz)}')