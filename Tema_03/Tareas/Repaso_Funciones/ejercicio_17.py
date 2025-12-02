# 17. Verificar si una cadena es un palíndromo.
# Crea una función que verifique si una cadena de texto 
# es un palíndromo (se lee igual de izquierda a derecha que de 
# derecha a izquierda).

def esPalindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    cadenaReversa = cadena[::-1]
    if cadena == cadenaReversa:
        print(f'La cadena {cadena} es un palindromo')
        
cadena = input("Introduce una cadena: ")
esPalindromo(cadena)