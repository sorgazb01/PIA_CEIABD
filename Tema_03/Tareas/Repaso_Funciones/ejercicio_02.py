# 2. Contar cuántas veces aparece un número en una lista.
# Escribe una función que cuente la cantidad de veces que un número 
# aparece en una lista dada.

def contarNumeroVecesLista(lista,  numero_buscar):
    cont = 0
    for numero in lista:
        if numero == numero_buscar:
            cont = cont + 1
    return cont

lista = [2,4,3,2,5,6,4,3,2,8,9,1,0,2,2]
numero = int(input("Introduce el numero a buscar en la lista:"))

resultado = contarNumeroVecesLista(lista, numero)

print(f"El número {numero} aparece {resultado} veces en la lista")