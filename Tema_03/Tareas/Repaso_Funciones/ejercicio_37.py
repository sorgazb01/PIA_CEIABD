# 37. Imprimir una tabla de multiplicar con números del 1 al 10.
# Crea una función que imprima una tabla de multiplicar para los números del 1 al 10.

def tablas_multiplicar():
    for i in range(1, 11):
        print(f'Tabla de multiplicar del {i}: ')
        for j in range(1, 11):
            print(f'{i} x {j} = {i * j}')
        print()

tablas_multiplicar()