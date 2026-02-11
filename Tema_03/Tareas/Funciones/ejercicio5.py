# Ejercicio 5. 🐌 El ascenso del Caracol 🐌
# Un caracol que asciende por una pared de 125 cm. Cada día recorre una distancia aleatoria de centímetros. 
# Durante la noche, al quedarse dormido, desciende 20 centímetros. 
# 
# Diseña una función que nos devuelva en cuantos días el caracol llega al final de la pared.
# DATOS:
# La distancia que recorre cada día viene en la siguiente lista:
# distancias_diarias = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]. Cada día recorre una de las cifras empezando por la izquierda.
# altura_muro = 125. Es la altura del muro
# caida_nocturna = 20 Son los centimetros que desciende durante la noche
# total_distancia_recorrida = 0 Distancia total recorrida por el caracol 
# 
# # Solución:

# Datos del problema
distancias_diarias = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
altura_muro = 125
caida_nocturna = 20

# Funcion que devuelve el numero de dias que tarda el caracol en subir el muro
def diasAscenso(distancias_diarias, altura_muro, caida_nocturna):
    # Total de dias y total de distancia recorrida
    totalDistancia = 0
    dias = 0
    # Recorremos el array de distancias diarias
    for distancia in distancias_diarias:
        # Aumentamos el dia y la distancia
        dias += 1
        totalDistancia += distancia
        # Si antes de finalizar el dia ha superado la altura
        # del muro devolvemos el numero de dias que ha tardado en
        # lograrlo
        if totalDistancia >= altura_muro:
            return dias
        # Sino restamos la distancia que desciende dormido
        else:
            totalDistancia -= caida_nocturna
    # En caso de que se acabe el array de dias y no haya alcanzado
    # la cima del muro devolvemos 0
    return 0

# Mostramos el resultado
dias = diasAscenso(distancias_diarias, altura_muro, caida_nocturna)
if dias != 0:
    print(f'El caracol llego a la cima en {dias} dias')
else:
    print('El caracol no llego a la cima')