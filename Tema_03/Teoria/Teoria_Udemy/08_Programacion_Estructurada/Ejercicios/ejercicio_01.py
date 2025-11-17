# Crea un programa que pida dos número enteros al usuario y 
# diga si alguno de ellos es múltiplo del otro. Crea una función 
# EsMultiplo que reciba los dos números, y devuelve si el primero es 
# múltiplo del segundo.

def esMultiplo (num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

num1 = int(input('Introduce el número 1: '))
num2 = int(input('Introduce el número 2: '))

if esMultiplo(num1, num2) == True:
    print(f'{num1} es multiplo de {num2}')
else:
    print(f'{num1} no es multiplo de {num2}')
