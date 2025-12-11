# 39. Determinar si dos listas son anagramas entre sí.
# Escribe una función que verifique si dos listas contienen los mismos elementos en
# cualquier orden.

lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]

def listasAnagramas(lista1, lista2):
    if sorted(lista1) == sorted(lista2):
        return True
    else:
        return False
    
if listasAnagramas(lista1, lista2):
    print("Las listas son anagramas entre sí.")
else:
    print("Las listas no son anagramas entre sí.")