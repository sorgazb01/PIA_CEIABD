# 11. Generar la secuencia de Fibonacci hasta N.
# Crea una función que genere los primeros N números de la secuencia 
# Fibonacci.

def fibonacci(limite):
    a = 0
    b = 1
    listaFibonacci = []
    while a < limite:
        listaFibonacci.append(a)
        a, b = b, a + b    
    for numero in listaFibonacci:
        print(numero)   
limite = int(input("Introduce hasta donde quieres obtener la secuencia de Fibonacci: "))
fibonacci(limite)