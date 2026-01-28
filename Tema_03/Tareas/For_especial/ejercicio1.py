# Ejercicios 1
# Dado un conjunto de números enteros, determina si hay algún número par en el conjunto.
# Si hay al menos un número par, imprime el primer número par encontrado. Si no hay ningún
# número par en el conjunto, imprime un mensaje indicando que no se encontró ningún número 
# par.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(f'Hay un numero par: {numero}')
        break
else:
    print('No se ha encontrado ningun numero par en la lista')