# Ejercicio 8
# Dadas dos tuplas:
# a) Crear una lista con todas las combinaciones que se pueden dar entre los elementos de las dos tuplas(pueden incluir repetidos)
# b) ¿Y sin repetidos?
# Ejemplos:
# Entrada : tupla1 =(7, 2), tupla2 =(7, 8)
# Salida : [(7, 7),(7, 8),(2, 7),(2, 8),(7, 7),(7, 2),(8, 7),(8, 2)]

# Tuplas de ejemplo
tupla1 = (7,2)
tupla2 = (7,8)

# Funcion para combiar los diferentes elementos de las tuplas
def combinarTuplas(tupla1, tupla2):
    lista_combinaciones = []
    # Primero combinamos cada uno de los elementos de la primera tupla con los de la segunda
    for elemento_tupla1 in tupla1:
        for elemento_tupla2 in tupla2:
            combinacion = (elemento_tupla1, elemento_tupla2)
            lista_combinaciones.append(combinacion)
    # Combinamos cada uno de los elementos de la segunda tupla con los de la primera        
    for elemento_tupla2 in tupla2:
        for elemento_tupla1 in tupla1:
            combinacion = (elemento_tupla2, elemento_tupla1)
            lista_combinaciones.append(combinacion)
    return lista_combinaciones
        
listaApartadoA = combinarTuplas(tupla1, tupla2)
print("Lista con repetidos: ")
print(listaApartadoA)

# Funcion para eliminar los elementos repetidos de una lista
def listaSinRepetidos(lista):
    lista_sin_repetidos = []
    for elemento in lista:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos

listaApartadoB = listaSinRepetidos(listaApartadoA)
print("Lista sin repetidos: ")
print(listaApartadoB)
