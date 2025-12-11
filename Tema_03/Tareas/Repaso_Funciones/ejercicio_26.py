# 26. Encontrar el número de veces que un carácter aparece en una cadena. 
# Crea una función que reciba una cadena y un carácter, y devuelva cuántas veces
# aparece ese carácter en la cadena.

def contadorCaracter(cadena, caracter):
    contador = 0
    for caracterCadena in cadena:
        if caracterCadena == caracter:
            contador += 1
    return contador

cadena = input('Introduce una cadena de texto: ')
caracter = input('Introduce el caracter a buscar: ')
print(f'El caracter {caracter} aparece {contadorCaracter(cadena, caracter)} veces en la cadena')