# 32. Generar una lista de números primos hasta N.
# Escribe una función que devuelva una lista de números primos hasta un número
# dado utilizando el método de la Criba de Eratóstenes.
from math import sqrt

# El metodo de la Criba de Eratostenes consiste en ir descartando todos los multiplos
# de cada numero para obtener asi la lista de los numeros primos
def primosLimite(limite):
    # Primero comprobamos que si el usuario nos ha pasado un limite menor de 2,
    # le devolvemos una lista vacia, no hay numeros primos menores de 2
    if limite < 2:
        return []
    
    # Creamos una lista booleana con todos los elementos a True
    # con la longitud hasta el limite incluido
    esPrimo = [True] * (limite + 1)
    
    # Asumimos que 0 y 1 no son primos
    esPrimo[0] = False
    esPrimo[1] = False
    
    # Recorremos desde 2 primer numero primo hasta la raiz cuadrade del limite,
    # porque los multiplos de numeros mayores ya estan marcados
    for numero in range(2, int(sqrt(limite)) + 1):
        # Si el número actual es primo
        if esPrimo[numero]:
            # Marcamos todos sus multiplos como no primos con el siguiente bucle
            for multiplo in range(numero * numero, limite + 1, numero):
                esPrimo[multiplo] = False

    # Devolvemos una lista con todos los números que sean primos
    primos = []
    for numero in range(limite + 1):
        if esPrimo[numero]:
            primos.append(numero)
    return primos

limite = int(input('Introduce un rango hasta el que obtener todos los numero primos: '))
primos = primosLimite(limite)
print(f'Numeros primos {primos}')
