# Ejercicio 4.
# Dadas una cadena verifique si es pangrama o no.
# Una cadena es pangrama cuando contiene todas las letras del alfabeto.
# a) Desarrolla un algoritmo que nos diga si un texto es pangrama.
# Entrada:
# Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol.
# Resultado:
# True, la cadena es un pangrama
# Versión 1 restando al alfabeto nuestra cadena, si el resultado es el set vacio, es un pangrama.
from string import ascii_lowercase as asc_lower

def esPangrama(texto):
    letrasTotales = set(asc_lower)
    letrasTexto = set(texto.lower())
    letrasFaltantes = letrasTotales - letrasTexto
    if(len(letrasFaltantes) == 0):
        return True
    else:
        return False
    
texto = 'Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol.'
resultado = esPangrama(texto)
print(f'Pangrama: {resultado}')