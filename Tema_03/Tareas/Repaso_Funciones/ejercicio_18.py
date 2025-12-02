# 18. Imprimir los divisores de un número.
# Escribe una función que imprima todos los divisores de un número 
# dado.

def divisoresNumero(numero):
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)

numero = int(input("Introduce un numero para obtener sus divisores: "))
divisoresNumero(numero)