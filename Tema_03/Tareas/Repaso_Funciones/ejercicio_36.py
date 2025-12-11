# 36. Detectar si una lista tiene elementos duplicados.
# Crea una función que determine si una lista contiene elementos duplicados.

lista = [1, 2, 3, 4, 5, 1]

def repetidosLista(lista):
    for elemento in lista:
        if lista.count(elemento) > 1:
            return True
    return False

print(repetidosLista(lista))