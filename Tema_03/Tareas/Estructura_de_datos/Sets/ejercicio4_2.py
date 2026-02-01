### Versión 2, contando los caracteres del alfabeto y los del set de nuestra cadena, si son iguales es pangrama
from string import ascii_lowercase as asc_lower

def esPangrama(texto):
    letrasTotales = set(asc_lower)
    letrasTexto = set()
    textoMinusculas = texto.lower()
    for letra in textoMinusculas:
        if letra.isalpha():
            letrasTexto.add(letra)
    letrasComunes = letrasTotales & letrasTexto
    if len(letrasTotales) == len(letrasComunes):
        return True
    else:
        return False
    
texto = 'Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol.'
resultado = esPangrama(texto)
print(f'Pangrama: {resultado}')