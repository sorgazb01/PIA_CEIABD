# Ejercicio 1
# Crea un Array 2D de 25 números aleatorios entre los 100 primeros números.
# 1) Pinta la matriz resultante.
# 2) De la matriz generada, quedate con los valores que sean múltiplos de 5.
# 3) Quedate con todos los valores pares o impares menores de 10.
# 4) Quedate con los valores que sean multiplos de 3 y que sean impares mayores de 20.
# 5) Une todos los resultados de los apartados 2-4 en un nuevo array 1D quedandote solo con los valores únicos.
# 6) Reestructura el array para convertirlo en uno 2D con tantas filas como elementos tenga.
# 7) Del nuevo array 2D, muestra su estructura, dimensiones y número de elementos

#1) Crea un Array 2D de 25 números aleatorios entre los 100 primeros números
import numpy as np

matriz = np.random.randint(0, 100, size=(5, 5))
print(matriz)

#2) Múltiplos de 5
multiplos5 = matriz[matriz % 5 == 0]
print("Múltiplos de 5:", multiplos5)

#3) Valores pares o impares menores de 10
menores10 = matriz[matriz < 10]
print("Pares o impares menores de 10:", menores10)

#4) Múltiplos de 3 que sean impares mayores de 20
resultado4 = matriz[(matriz % 3 == 0) & (matriz % 2 != 0) & (matriz > 20)]
print("Múltiplos de 3, impares y mayores de 20:", resultado4)

#5) Une todos los resultados de los apartados 2-4 en un nuevo array 1D con valores únicos
union = np.unique(np.concatenate([multiplos5, menores10, resultado4]))
print("Array unido con valores únicos:", union)

#6) Reestructura el array para que sea 2D, con tantas filas como elementos tenga
array2d = union.reshape(-1, 1)
print(array2d)

#7) Muestra la estructura, dimensiones y número de elementos del array
print("Estructura (shape):", array2d.shape)
print("Dimensiones (ndim):", array2d.ndim)
print("Número de elementos (size):", array2d.size)