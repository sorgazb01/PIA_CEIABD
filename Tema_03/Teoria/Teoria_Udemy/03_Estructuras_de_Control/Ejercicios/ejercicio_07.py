# Realizar un algoritmo que muestre la tabla de multiplicar de un número
# introducido por teclado

numero = int(input('Introduce un número para obtener la tabla de multiplicar: '))

for var in range(0,11):
    print(numero,' x ',var,' = ',numero*var)
