# 3. Palabra de Mayor Valor
# Dada una cadena de palabras, debe encontrar la palabra con la puntuación 
# más alta. Cada letra de una palabra obtiene puntos según su posición en 
# el alfabeto: a = 1, b = 2, c = 3, etc.
# Debe devolver la palabra con la puntuación más alta dentro de la frase.
# Si dos palabras tienen el mismo puntaje, devuelve la palabra que aparece 
# más temprano en la cadena original.
# Todas las letras serán minúsculas y todas las entradas serán válidas.
# Escribe una función para resolver el problema.

# Funcion para obtener la puntuacion de la palabra
def puntuacionPalabra(palabra):
    puntuacion = 0
    # Recorremos letra a letra la palabra y sumamos su puntuacion al total
    for letra in palabra:
        puntuacion += ord(letra) - ord('a') + 1
    return puntuacion

# Funcion para encontrar la palabra de mayor puntuacion de la frase
def palabraMayorValor(cadena):
    # Separamos la frase en palabras
    palabras = cadena.split()
    # Asumimos que la primera palabra es la de mayor puntuacion
    mejorPalabra = palabras[0]
    puntuacionMejorPalabra = puntuacionPalabra(mejorPalabra)
    # Recorremos el resto de palabras de la frase
    for palabra in palabras[1:]:
        # Obtenemos la puntuacion de la palabra que estamos puntuando en
        # cada iteracion del bucle
        puntuacion = puntuacionPalabra(palabra)
        # Si la puntuacion es mejor la asignamos como la mejor palabra
        if puntuacion > puntuacionMejorPalabra:
            mejorPalabra = palabra
            puntuacionMejorPalabra = puntuacion
    return mejorPalabra

frase = input('Introduce una frase para ver cual es la palabra de mayor valor: ')
print(f'La palabra de mayor valor es: {palabraMayorValor(frase)}')