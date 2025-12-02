# 1. Suma de números pares en un rango dado.
# Crea una función que sume los números pares en un rango de 1 a N 
# (inclusive).

def sumaParesRango(limite):
    suma = 0
    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            suma = suma + numero
    return suma

limite = int(input("Introduce el límite hasta el cual quieres sumar los números pares:"))

resultado = sumaParesRango(limite)

print(f"La suma de todos números pares del rango es: {resultado}")