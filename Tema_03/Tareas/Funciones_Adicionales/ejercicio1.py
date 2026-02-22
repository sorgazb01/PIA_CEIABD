# 1. La codicia
# La codicia es un juego de dados jugado con cinco dados de seis lados. Tu misión, 
# si eliges aceptarla, es anotar la puntuación de acuerdo a las siguientes reglas: 
#   Tres 1 => 1000 puntos
#   Tres 6 = 600 puntos
#   Tres 5 = 500 puntos
#   Tres 4 => 400 puntos
#   Tres 3 => 300 puntos
#   Tres 2 => 200 puntos
#   Uno 1 => 100 puntos
#   Uno 5 => 50 puntos
# Siempre se le dará una matriz con cinco valores de dados de seis lados.
# Un solo dado solo se puede contar una vez en cada tirada. Por ejemplo, un "5"
# solo puede contar como parte de un triplete (contribuyendo a los 500 puntos) o 
# como un solo 50 puntos, pero no ambos en el mismo rollo.
# 
# Ejemplo de puntuación:
# Sacar puntaje
# 5 1 3 4 1 50   + 2 * 100 = 250
# 1 1 1 3 1 1000 + 100     = 1100
# 2 4 4 5 4 400  + 50      = 450
import random

# Funcion para generar una tirada aleatoria de los dados
def tirarDados(numeroDados):
    # Lista que guardara la tirada de cada dado
    tiradas = []
    # Generamos una tirada aleatoria por cada dado y la guardamos
    # en la lista
    for _ in range(numeroDados):
        tirada = random.randint(1,6)
        tiradas.append(tirada)
    return tiradas

# Funcionn para calcular la puntuacion de la tirada
def codicia(tirada):
    # Total de puntuacion
    puntuacion = 0
    # Contador de cada una de las caras que se han obtenido en la tirada
    uno = tirada.count(1)
    dos = tirada.count(2)
    tres = tirada.count(3)
    cuatro = tirada.count(4)
    cinco = tirada.count(5)
    seis = tirada.count(6)
    # Obtenemos la puntuacion en funcion de las reglas del juego
    # Unos
    # Si hay un triple 1 sumanos mil puntos
    # restamos el triple 1 al total de unos y 
    # si hay aun mas unos sumamos 100 puntos por cada uno
    if uno >= 3:
        puntuacion += 1000
        uno -= 3
    if uno > 0:
        puntuacion += uno * 100
    # Dos
    # Si hay un triple 2 sumanos 200 puntos
    if dos >= 3:
        puntuacion += 200
    # Tres
    # Si hay un triple 3 sumanos 300 puntos
    if tres >= 3:
        puntuacion += 300
    # Cuatros
    # Si hay un triple 4 sumanos 400 puntos
    if cuatro >= 3:
        puntuacion += 400
    # Cincos
    # Si hay un triple 5 sumanos 500 puntos
    # restamos el triple 5 al total de cincos y 
    # si hay aun mas cincos sumamos 50 puntos por cada uno
    if cinco >= 3:
        puntuacion += 500
        cinco -= 3
    if cinco > 0:
        puntuacion += cinco * 50
    # Seis
    # Si hay un triple 6 sumanos 600 puntos
    if seis >= 3:
        puntuacion += 600
    return puntuacion

numeroDados = 5
dados = tirarDados(numeroDados)
print(f'Tirda: {dados}')
puntuacion = codicia(dados)
print(f'Puntuacion de la tirada: {puntuacion}')