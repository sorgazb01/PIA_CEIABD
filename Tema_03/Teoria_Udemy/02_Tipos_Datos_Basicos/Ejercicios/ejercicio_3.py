# Dadas dos variables nméricas A y B, que el usuario debe teclear,
# se pide realizar un algoritmo que intercambie los valores de ambas
# y muestre cuanto valen al final las dos variables.

a = int(input("Introduce el valor de A: "))
b = int(input("Introduce el valor de B: "))

print(f"Valores iniciales: A = {a}, B = {b}")

aux = a
a = b
b = aux

print(f"Valores intercambiados: A = {a}, B = {b}")