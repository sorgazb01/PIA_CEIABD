# 6. Verificar si un número es par o impar.
# Implementa una función que reciba un número y determine 
# si es par o impar.

def esParOImpar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par.")
    else:
        print(f"El numero {numero} es impar.")
        
numero = int(input("Introduce un numero: "))
esParOImpar(numero)