# 5- Encontrar el Atípico
# Recibimos una lista (que tendrá una longitud de al menos 3, pero podría ser 
# muy grande) que contiene enteros. La lista está compuesta por enteros impares 
# o enteramente por enteros pares, excepto por un solo entero N. Escribe una función 
# que tome la lista como argumento y devuelva este N. "atípico".
# 
# Ejemplos
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Debería devolver: 11 (el único número impar)
# [160, 3, 1719, 19, 11, 13, -21]
# Debería devolver: 160 (el único número par)

# Funcion para encontrar el elemento atipico de una lista
def encontrarNumeroAtipico(lista):
    # Lista de pares e impares
    pares = []
    impares = []
    # Recorremos cada numero de la lista
    for numero in lista:
        # Si el numero es para lo ponemos en la lista de pares
        if numero % 2 == 0:
            pares.append(numero)
        # Si no en la de impares
        else:
            impares.append(numero)
    # Si en la lista de pares solo hay un numero ese es el numero atipico
    if len(pares) == 1:
        return pares[0]
    # Si no el numero atipico es impar
    else:
        return impares[0]
    
print(f'El elemento atipico de la lista es: {encontrarNumeroAtipico([2, 4, 0, 100, 4, 11, 2602, 36])}')