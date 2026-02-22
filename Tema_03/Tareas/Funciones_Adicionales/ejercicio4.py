# 4. Encontrar Perdidos
# Una progresión aritmética se define como aquella en la que hay una diferencia 
# constante entre los términos consecutivos de una serie dada de números. 
# Nos proporcionan elementos consecutivos de una progresión aritmética. 
# Sin embargo, hay un problema: faltan exactamente un término de la serie original 
# del conjunto de números que se le han dado. El resto de la serie dada es la misma 
# que la AP original. Encuentra el término que falta.
# Debe escribir una función que reciba una lista, el tamaño de la lista siempre 
# será de al menos 3 números. El término faltante nunca será el primero o el último.

# Ejemplo
# encontrar_perdido ([1, 3, 5, 9, 11]) == 7
# lista=[1, 2, 3, 4, 6, 7, 8, 9]    
# lista2=[1, 3, 4, 5, 6, 7, 8, 9]
# encontrar_perdido(lista) => 5
# encontrar_perdido(lista2) => 2

# Funcion para encontrar el elemento perdido de una lista aritmetica
def encontrarPerdido(lista):
    elementoPerdido = 0
    # Obtenemos la distancia que hay entre los numeros de la lista aritmetica
    distanciaNumeros = (lista[-1] - lista[0]) // len(lista)
    # Recorremos la lista y vamos comparando la distancia entra cada numero
    for i in range(len(lista)):
        # Si la distancia entre un numero y el siguiente no es igual
        # a la distancia entre numeros hemos encontrado el elemento perdido.
        # para obtener el elemento sumamos la distancia al numero actual del bucle
        if lista[i + 1] - lista[i] != distanciaNumeros:
            elementoPerdido = lista[i] + distanciaNumeros
            break
    return elementoPerdido

print(encontrarPerdido([1, 3, 5, 9, 11]))         
print(encontrarPerdido([1, 2, 3, 4, 6, 7, 8, 9])) 
print(encontrarPerdido([1, 3, 4, 5, 6, 7, 8, 9])) 