# 14. Calcular el factorial de un número.
# Crea una función que calcule el factorial de un número de manera recursiva o
# iterativa.

def factorial(numero):
    if numero < 0:
        return -1
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado = resultado * i
        return resultado
    
numero = int(input("Introduce un número para obtener su factorial: "))
resultado = factorial(numero)

if resultado == -1:
    print("No se puede calcular el factorial de un numero negativo")
else:
    print(f"El factorial de {numero} es: {resultado}")