# 17. Verificar si una cadena es un palíndromo.
# Crea una función que verifique si una cadena de texto 
# es un palíndromo (se lee igual de izquierda a derecha que de 
# derecha a izquierda).

# Una cadena es un palindromo si se lee igual de izquierda a derecha
def esPalindromo(cadena):
    # Eliminamos cualquier espacio en la cadena y pasamos todos
    # los caracteres a minusculas para realizar las comprobaciones
    cadena = cadena.replace(" ", "").lower()
    # Como una cadena se puede tratar como un array, la invertimos
    cadenaReversa = cadena[::-1]
    # Comprobamos que las cadenas sean iguales
    if cadena == cadenaReversa:
        print(f'La cadena {cadena} es un palindromo')
    else:
        print(f'La cadena {cadena} no es un palindromo')
        
cadena = input("Introduce una cadena: ")
esPalindromo(cadena)