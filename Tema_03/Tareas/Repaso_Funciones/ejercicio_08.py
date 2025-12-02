# 8. Contar las vocales en una cadena de texto.
# Escribe una función que cuente cuántas vocales (mayúsculas y minúsculas)
# hay en una cadena de texto.

vocales = "aeiouáéíóú"

def contadorVocales(cadena):
    contador = 0
    for palabra in cadena:
        for letra in palabra:
            if letra.lower() in vocales:
                contador = contador + 1
    return contador

cadena = input("Introduce una cadena para contar sus vocales: ")
totalVocales = contadorVocales(cadena)
print(f"La cadena {cadena} tiene {totalVocales} vocales.")