# Ejercicio 4
# 1. Crea los siguientes Arrays:
# a será un array 2D con valores aleatorios normales y estructura 3x3.
# b será un array 1D con 3 elementos aletarorios entre 3-6.    
# 2. Suma los dos arrays y al resultado aplicale la raiz cuadrada.
# 3. Redondea el array resultante a dos decimales.
# 4. Crea un array denominado c que sea 2D 5x5 con números aleatorios entre 0-60.
# 5. Ordena cada fila.
# 6. Aplica la inversa:
# A cada fila del array resultante del apartado 5.
# A cada columna.
# A toda la matriz
# 7. Saca la matriz traspuesta de c.

import numpy as np

#1) Crea un array 'a' de 3x3 con valores aleatorios de distribución normal
#   y un array 'b' de 1D con 3 elementos aleatorios entre 3 y 6
a = np.random.randn(3, 3)
b = np.random.randint(3, 7, size=3)
print("Array a (3x3 normal):")
print(a)
print("Array b (1D randint 3-6):")
print(b)

#2) Suma a + b y aplica la raíz cuadrada al resultado
suma = a + b
raiz = np.sqrt(np.abs(suma))
print("Suma a + b:")
print(suma)
print("Raíz cuadrada de la suma:")
print(raiz)

#3) Redondea a 2 decimales
raizRedondeada = np.round(raiz, 2)
print("Raíz cuadrada redondeada a 2 decimales:")
print(raizRedondeada)

#4) Crea un array 'c' de 5x5 con valores aleatorios entre 0 y 60
c = np.random.randint(0, 61, size=(5, 5))
print("Array c (5x5 randint 0-60):")
print(c)

#5) Ordena cada fila del array c
cOrdenado = np.sort(c, axis=1)
print("Array c con filas ordenadas:")
print(cOrdenado)

#6) Aplica flip a filas, columnas y a toda la matriz
flipFilas = np.flip(c, axis=1)
flipColumnas = np.flip(c, axis=0)
flipTotal = np.flip(c)
print("Flip filas (eje 1):")
print(flipFilas)
print("Flip columnas (eje 0):")
print(flipColumnas)
print("Flip total:")
print(flipTotal)

#7) Transpuesta de c
cTranspuesta = c.T
print("Transpuesta de c:")
print(cTranspuesta)