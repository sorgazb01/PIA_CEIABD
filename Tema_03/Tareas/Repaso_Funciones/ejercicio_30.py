# 30. Imprimir el reverso de una lista.
# Implementa una función que reciba una lista y devuelva su reverso.

lista = [1, 2, 3, 4, 5]

def listaReversa(lista):
    listaReversa = []
    for i in range(len(lista)-1, -1, -1):
        listaReversa.append(lista[i])
    return listaReversa

print(f'Lista original: {lista}')
print(f'Lista reversa: {listaReversa(lista)}')