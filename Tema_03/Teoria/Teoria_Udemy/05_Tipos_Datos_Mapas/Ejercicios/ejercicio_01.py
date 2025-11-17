# Escribe un programa que lea una cadena y devuelva un diccionario 
# con la cantidad de apariciones de cada carácter en la cadena.

diccionario = {}

cadena = input('Introduce una frase: ')

for caracter in cadena :
    if caracter in diccionario:
        diccionario[caracter] += 1
    else:
         diccionario[caracter] = 1
         
for clave, valor in diccionario.items():
    print(f'Caracter: {clave}, Numero de apariciones: {valor}')