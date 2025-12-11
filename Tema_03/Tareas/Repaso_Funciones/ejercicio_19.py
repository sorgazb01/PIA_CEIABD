# 19. Verificar si un número es perfecto.
# Implementa una función que determine si un número es perfecto (la suma de sus
# divisores propios es igual al número).

# Un numero perfecto es aquel en el que la suma de sus divisores 
# es igual al propio numero
def esNumeroPerfecto(numero):
    # Creamos una variable que almacenara la suma de los divisores
    sumaDivisores = 0
    # Creamos un bucle que recorra toda la lista de divisores
    # hasta el propio numero
    for i in range(1, numero):
        # Comprobamos que el elemento del bucle sea divisor
        if numero % i == 0:
            # Si lo es lo sumanos a la lista de divisores
            sumaDivisores = sumaDivisores + i
    # Comprobamos que la suma sea igual al numero
    if sumaDivisores == numero:
        print(f"El numero {numero} es un numero perfecto")
    else:
        print(f"El numero {numero} no es un numero perfecto")

numero = int(input("Introduce un numero"))
esNumeroPerfecto(numero)