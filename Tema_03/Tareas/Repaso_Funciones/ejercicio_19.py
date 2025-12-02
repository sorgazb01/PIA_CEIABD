# 19. Verificar si un número es perfecto.
# Implementa una función que determine si un número es perfecto (la suma de sus
# divisores propios es igual al número).

def esNumeroPerfecto(numero):
    sumaDivisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            sumaDivisores = sumaDivisores + i
    if sumaDivisores == numero:
        print(f"El numero {numero} es un numero perfecto")
    else:
        print(f"El numero {numero} no es un numero perfecto")

numero = int(input("Introduce un numero"))
esNumeroPerfecto(numero)