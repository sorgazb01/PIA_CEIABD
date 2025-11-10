# Algoritmo que pida números hasta que se introduzca un cero. Debe imprmir la suma
# y la media de todos los números introducidos.

contador = 0
suma = 0

num = int(input('Número (0 para salir:)'))
while num != 0:
    suma = suma + num
    contador = contador + 1
    num = int(input('Número (0 para salir:)'))

if contador > 0:
    media = suma / contador
else:
    media = 0

print('Suma de números: ', suma)
print('Media: ', media)