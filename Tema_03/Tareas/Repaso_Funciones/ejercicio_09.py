# 9. Imprimir números en orden descendente.
# Crea una función que imprima los números de un rango de N a 1 de
# manera descendente.

def imprimirDescendente(limite):
    for numero in range(limite, 0, -1):
        print(numero)
        
limite = int(input("Introduce un número para realizar la cuenta atrás: "))
imprimirDescendente(limite)