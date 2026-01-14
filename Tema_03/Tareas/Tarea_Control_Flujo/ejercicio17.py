# Ejercicio 17. Juego del ahorcado.
# 1- Numero de intentos del juego será 10.

# 2- Tendremos una lista de palabras. Lo ideal seria cargar un fichero con todas las palabras del español, 
# pero por simplificar añadiremos 10 palabras a una lista.

# 3- Cogeremos una de forma aletoria de esta lista de palabras. Una vez hecho, 
# dará comienzo el juego del ahorcado. **Nota:** investigar la forma de coger un elemento de forma aletoria de una lista de valores.

# 4- Se nos irá pidiendo una letra en cada ronda, si acertamos se descubrirán las posiciones de la palabra que contengan esa letra. 
# Si fallamos se mantendrán ocultas con un * o un #.

# 5- Tras introducir letra, el juego preguntará al jugador si quiere resolver, si la respuesta es Si, pedirá la palabra al jugador. 
# Podrán ocurrir 3 situaciones:  
# 1.   **El jugador acierta.** La palabra introducida es correcta, el juego acaba con un mensaje de enhorabuena.
# 2.   **No acierta.** El juego continua.
# 3.   Ronda 10 y no se acierta. **El jugador pierde automáticamente.**

import random as rd

numeroIntentos = 10

listaPalabras = ['casa', 'coche', 'manzana', 'futbol', 'zapatilla', 'telefono', 'ordenador', 'mochila', 'cuadro', 'ventana']

palabraJuego = rd.choice(listaPalabras)
palabraOculta = ['*'] * len(palabraJuego)

haAcertado = False

while not haAcertado:
    for i in range(1, numeroIntentos + 1):
        print(f'Ronda {i}:')
        while True:
            letra = input('Di una letra: ').lower()
            if len(letra) == 1:
                break
            else:
                print('Introduce solo una letra.')
        if letra in palabraJuego:
            for i in range(0,len(palabraJuego)):
                if letra == palabraJuego[i]:
                    palabraOculta[i] = letra
        print(''.join(palabraOculta))
        resolver = input('Quieres resolver? (S/n): ').lower()
        if resolver == 's':
            palabra = input('Di la palabra: ').lower()
            if palabra == palabraJuego:
                print(f'ENHORABUENA, HAS ACERTADO. La palabra era {palabraJuego}')
                haAcertado = True
                break
    if haAcertado == False:
        print(f'LO SIENTO HAS PERDIDO, EL JUEGO SE ACABO. La palabra era {palabraJuego}')
        break
