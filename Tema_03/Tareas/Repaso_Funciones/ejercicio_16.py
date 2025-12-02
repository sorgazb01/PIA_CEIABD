# 16. Imprimir los números de Fibonacci menores que N.
# Escribe una función que imprima todos los números de Fibonacci 
# menores que un número dado.

def menoresLimiteFibonacci(limite):
    a, b = 0, 1
    while a < limite:
        print(a)
        a, b = b, a + b
        
limite = int(input("Introduce un limite: "))
menoresLimiteFibonacci(limite)