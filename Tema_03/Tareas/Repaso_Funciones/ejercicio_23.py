# 23. Crear una lista de números que son múltiplos de 3 y 5.
# Crea una función que devuelva una lista de números múltiplos de 3 o 5 en un rango
# de 1 a N.

def multiplos3_5(limite):
    listaMultiplos = []
    for i in range(1, limite + 1):
        if i % 3 == 0 or i % 5 == 0:
            listaMultiplos.append(i)
    return listaMultiplos


limite = int(input('Introduce el rango de numeros que quieres obtener la lista de multipos de 3 y 5: '))
listaMultiplos = multiplos3_5(limite)
print(f'Los numero que son multiplos de 3 y de 5 en el rango de 1 a {limite} son: ')
for numero in listaMultiplos:
    print(numero)