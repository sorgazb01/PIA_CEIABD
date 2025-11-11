# Realizar un programa que inicialice una lista con 1o valores aleatorios (del 1 al 10)
# y posteriormente muestre en pantalla cada elemento de la lista junto con su 
# cuadrado y su cubo.

import random

lista_numeros = []

for indice in range(1,11):
    lista_numeros.append(random.randint(1,10))
    
for numero in lista_numeros:
    print(f'Numero {numero}')
    print(f'Cuadrado -> {pow(numero,2)}')
    print(f'Cubo -> {pow(numero,3)}')