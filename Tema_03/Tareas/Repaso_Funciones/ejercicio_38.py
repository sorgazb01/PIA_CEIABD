# 38. Verificar si una lista está ordenada de forma ascendente.
# Crea una función que determine si una lista de números está ordenada de manera
# ascendente.

lista = [1, 2, 3, 4, 5]

def listaOrdenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

if listaOrdenada(lista):
    print("La lista está ordenada de forma ascendente.")
else:
    print("La lista no está ordenada de forma ascendente.")