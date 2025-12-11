# 34. Contar la frecuencia de cada letra en una cadena de texto.
# Implementa una función que devuelva un diccionario con la frecuencia de aparición
# de cada letra en una cadena.

caracteresEspeciales = '''!@#$%^&*()_+-=[]{}|;':",.<>?/`~¡¿ '''

def frecuenciaLetras(cadena):
    diccionarioLetras = {}
    for letra in cadena :
        if letra not in caracteresEspeciales:
            letra = letra.lower()
            if letra in diccionarioLetras:
                diccionarioLetras[letra] += 1
            else:
                diccionarioLetras[letra] = 1
    return diccionarioLetras

cadena = input('Introduce una cadena de texto: ')
diccionarioLetras = frecuenciaLetras(cadena)
for letra, frecuencia in diccionarioLetras.items():
    print(f'{letra} -> {frecuencia}')