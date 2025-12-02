# 3. Encontrar el número más grande en una lista.
# Implementa una función que encuentre y devuelva el número mayor 
# en una lista de enteros.

def numeroMayorLista(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

lista = [0, 11, 43434, 665, 12, 1, 88, 858321, 145]
numeroMayor = numeroMayorLista(lista)
print(f"El numero mayor en la lista es: {numeroMayor}")