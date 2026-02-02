# Ejercicio 2 - El buscador de Aes.
# Dada una frase cualquiera, transforma cada palabra aplicando el siguiente criterio:
# Si la palabra contiene al menos una a la ponemos en mayuscula.
# Si la palabra NO contiene ninguna a irá con formato de título.
# a) Resuelve el problema sin comprensiones.
# b) Soluciona el ejercicio usando comprensión.

#a)
frase = 'En un lugar de La Mancha de cuyo nombre no quiero acordarme'

def convertirFrase(frase):
    nuevaFrase = ''
    for palabra in frase.split():
        if 'a' in palabra or 'A' in palabra:
            nuevaFrase += palabra.upper() + ' '
        else:
            nuevaFrase += palabra.capitalize() + ' '
    return nuevaFrase.strip()

print(convertirFrase(frase))

#b)
def convertirFraseCompresion(frase):
    return ' '.join([palabra.upper() if 'a' in palabra.lower() else palabra.capitalize() for palabra in frase.split()])

print(convertirFraseCompresion(frase))