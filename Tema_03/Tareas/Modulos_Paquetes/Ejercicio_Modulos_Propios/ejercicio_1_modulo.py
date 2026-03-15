# Importamos el modulo random
import random

# Funcion para generar la lista de numeros aleatorios
def generarLista():
    listaRandom = []
    for _ in range(7):
        listaRandom.append(random.randint(0, 100))
    return listaRandom

# Funcion para mostrar la lista de numeros
def mostrarLista(lista):
    print(lista)

# Funcion para ordenar la lista de numeros
def ordenarLista(lista):
    return sorted(lista)