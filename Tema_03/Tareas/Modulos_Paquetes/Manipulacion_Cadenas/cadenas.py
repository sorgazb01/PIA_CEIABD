def invertir(cadena):
    return cadena[::-1]


def contar_vocales(cadena):
    vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    return sum(1 for c in cadena if c in vocales)


def a_mayusculas(cadena):
    return cadena.upper()


def a_minusculas(cadena):
    return cadena.lower()