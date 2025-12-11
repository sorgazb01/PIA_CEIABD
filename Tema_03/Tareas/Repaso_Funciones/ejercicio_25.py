# 25. Contar las palabras de una cadena de texto.
# Escribe una función que cuente cuántas palabras contiene una cadena de texto.

def contadorPalabras(cadena):
    palabras = cadena.split()
    return len(palabras)

cadena = input('Introduce una cadena: ')
print(f'La cadena tiene {contadorPalabras(cadena)} palabras')