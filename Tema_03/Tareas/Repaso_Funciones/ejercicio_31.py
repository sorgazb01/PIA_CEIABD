# 31. Ordenar una lista de números de menor a mayor.
# Crea una función que ordene una lista de números en orden ascendente utilizando
# un algoritmo de ordenamiento sencillo (como burbuja).

lista = [64, 34, 25, 12, 22, 11, 90]

def ordenarListaMenorMayor(lista):
    longitud = len(lista)
    for i in range(longitud):
        for j in range(0, longitud-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print(f'Lista original: {lista}')
print(f'Lista ordenada de menor a mayor: {ordenarListaMenorMayor(lista)}')