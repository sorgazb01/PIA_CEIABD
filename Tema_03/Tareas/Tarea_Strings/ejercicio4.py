# 4- Escribir un programa que pida al usuario que introduzca una frase en la consola y 2 vocales, y después muestre 
# por pantalla la misma frase pero con las vocales introducidas en mayúsculas.

cadena = input('Introduce una cadena: ')

vocales = 'aeiou'

while True:
    vocal1 = input('Introduce la primera vocal: ').lower()
    if len(vocal1) != 1 and vocal1 not in vocales:
        print('Introduce una unica vocal por favor')
    else:
        break

while True:
    vocal2 = input('Introduce la segunda vocal: ').lower()
    if len(vocal2) != 1 and vocal2 not in vocales:
        print('Introduce una unica vocal por favor')
    else:
        break

cadenaNueva = cadena.replace(vocal1, vocal1.upper()).replace(vocal2, vocal2.upper())

print(f'La cadena original era: {cadena}')
print(f'La nueva cadena es: {cadenaNueva}')