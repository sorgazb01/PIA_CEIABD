# Problema 1. División de una lista de enteros.
# Escribe una función que reciba por parámetro una lista de enteros y devuelva
# dos listas: una con los valores negativos que tuviera y otra con los positivos.
# Ambas listas deben estar ordenadas ascendentemente

def division_enteros(numeros):
    positivos = []
    negativos = []
    for numero in numeros:
        if numero >= 0:
            positivos.append(numero)
        else:
            negativos.append(numero)
    
    positivos.sort()
    negativos.sort()

    print("Números positivos:",positivos)
    print("Números negativos:",negativos)

print(division_enteros([3, -1, -5, 2, -2, 4]))