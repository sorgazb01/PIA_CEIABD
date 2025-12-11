# 27. Imprimir todos los números primos en un rango dado.
# Crea una función que imprima todos los números primos en un rango de 1 a N.

def esPrimo(numero):
    if numero <= 1:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
                break
            else:
                return True
            
def imprimirPrimosRango(limite):
    for numero in range(2, limite + 1):
        if esPrimo(numero):
            print(numero)

limite = int(input('Introduce un rango hasta el que mostrar todos los numeros primos de ese rango: '))
imprimirPrimosRango(limite)