# Ejercicio 9. Números consecutivos.
# Diseña un programa que muestre aquellos números que se encuentran repetidos exactamente 3 veces.
# Ejemplos:
# Entrada: [4, 5, 5, 5, 3, 8]
# Salida: 5
# Entrada: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Salida : 1, 22

# Función que devuelve una lista con los números que se repiten x veces.
def numerosRepetidos(lista, numeroVeces):
    listaNumerosRepetidos = []
    for numero in lista:
        if lista.count(numero) == numeroVeces and numero not in listaNumerosRepetidos:
            listaNumerosRepetidos.append(numero)
    return listaNumerosRepetidos

#  Función que muestra el resultado del ejercicio
def mostrarResultado(lista, numeroVeces):
    if len(lista) == 0:
        print(f'No hay números que se repitan {numeroVeces} veces en la lista.')
    else:
        print(f'Los números que se repiten {numeroVeces} veces son: {lista}.')

numeroVeces = 3
lista = [1, 1, 1, 64, 23, 64, 22, 22, 22]
numerosRepetidos = numerosRepetidos(lista, numeroVeces)

mostrarResultado(numerosRepetidos, numeroVeces)
