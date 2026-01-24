# Ejercicio 7

# Nos han encargado que diseñemos un programa para detectar bombas de una lista de N números.
# Serán bombas todos los números que contengan el número que introduzca el jefe de los TEDAX por teclado(0-9)
# lista_con_bombas=[11, 107, 17, 67, 99, 45, 37, 87, 1007, 2007, 2027, 10007, 7, 1, 15, 81, 91, 88, 307]
# a) Analiza la lista para indicar el jefe TEDAX si hay bomba o la lista es segura.
# b) Modifica el programa para en caso de existir bombas, indicar el nº y la posición en la que se encuentra de la lista de bombas

lista_con_bombas=[11, 107, 17, 67, 99, 45, 37, 87, 1007, 2007, 2027, 10007, 7, 1, 15, 81, 91, 88, 307]

def leerNumero():
    while True:
        numero = input("Introduce un numero del 0 al 9: ")
        if len(numero) == 1:
            return numero
        else:
            print('Error, debes introducir un numero entre el 0 y el 9, intentalo de nuevo. ')

def comprobarLista(lista, numero):
    bombasEncontradas = []
    for bomba in lista:
        if numero in str(bomba):
            bombasEncontradas.append(bomba)
    return bombasEncontradas   

def esListaSegura(bombas, lista):
    if len(bombas) == 0:
        print('La lista es segura, no hay bombas. ')
    else:
        print(f'La lista no es segura, hay {len(bombas)} bombas.')
        mostrarBombas(bombas, lista) 

def mostrarBombas(bombas, lista):
    for bomba in bombas:
        posicion = lista.index(bomba)
        print(f'Bomba: {bomba} -> Posicion: {posicion + 1}.')       

numero = leerNumero()

bombas = comprobarLista(lista_con_bombas, numero)

esListaSegura(bombas, lista_con_bombas)
