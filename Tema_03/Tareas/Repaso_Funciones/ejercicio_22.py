# 22. Calcular la suma de los números primos hasta N.
# Implementa una función que calcule la suma de los números primos en un rango
# hasta un número dado.

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
            
def sumaPrimosRango(limite):
    sumaPrimos = 0
    for numero in range(2, limite + 1):
        if esPrimo(numero):
            sumaPrimos += numero
    return sumaPrimos

limite = int(input('Introduce un rango hasta el que sumar todos los numeros primos de ese rango: '))
print(f'La suma de todos los numeros primos del rango es: {sumaPrimosRango(limite)}')