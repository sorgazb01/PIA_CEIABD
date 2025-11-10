# Crea una aplicación que pida un número y calcule su factorial (El factorial
# de un número es el producto de todos los enteros entre 1 y el propio números
# representado por el número seguido de un signo de exclamación.
# Por ejemplo 5! = 1*2*3*4*5 = 120)

resultado = 1
numero = int(input('Introduce un número: '))
contador = 2

while contador <= numero:
    resultado = resultado * contador
    contador = contador + 1
print('El resultado es', resultado)