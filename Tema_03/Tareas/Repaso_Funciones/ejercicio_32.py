# 32. Generar una lista de números primos hasta N.
# Escribe una función que devuelva una lista de números primos hasta un número
# dado utilizando el método de la Criba de Eratóstenes.

def generarPrimosHastaLimite(limite):
    primos = []
    esPrimo = [True] * (limite + 1)
    esPrimo[0] = esPrimo[1] = False

    for numero in range(2, limite + 1):
        if esPrimo[numero]:
            primos.append(numero)
            for multiplo in range(numero * numero, limite + 1, numero):
                esPrimo[multiplo] = False

    return primos


limite = int(input('Introduce un numero limite para generar la lista de numeros primos: '))
listaPrimos = generarPrimosHastaLimite(limite)
print(f'La lista de numeros primos hasta {limite} es: ')
for primo in listaPrimos:
    print(primo)
