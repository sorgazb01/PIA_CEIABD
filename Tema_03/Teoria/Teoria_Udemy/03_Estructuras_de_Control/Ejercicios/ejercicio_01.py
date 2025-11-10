# Algoritmo que pida al usuario un numero y diga si positivo, negativo o cero

numero = int(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo.")
elif  numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")