# 35. Crear un programa que calcule el promedio de una lista de números.
# Escribe una función que calcule el promedio de los números en una lista.

listaNumeros = []

def calcularPromedio(lista):
    promedio = 0
    if len(lista) != 0:
        suma = sum(lista)
        promedio = suma / len(lista)
    return promedio

print("El promedio de la lista es:", calcularPromedio(listaNumeros))