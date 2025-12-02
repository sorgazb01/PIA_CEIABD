# 12. Suma de dígitos de un número.
# Escribe una función que reciba un número y devuelva la suma de 
# sus dígitos.

def sumaPartes(numero):
    suma = 0
    for digito in numero:
        suma = suma + int(digito)
    return suma

numero = input("Introduce un número: ")
resultado = sumaPartes(numero)

print(f"La suma de los digitos de {numero} es: {resultado}")