# Ejercicio 9
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido.
# Tenemos que hacer dos bucles:
# 1- Bucle para el nº de filas
# 2- Bucle para el nº de asteriscos por fila.

numero = int(input('Introduce la altura del triangulo: '))

for fila in range(1, numero + 1):
    for asteriscto in range(fila):
        print('*', end='')
    print()