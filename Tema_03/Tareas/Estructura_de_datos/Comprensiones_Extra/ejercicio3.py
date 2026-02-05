# 3 Lanzamiento de 100mil dados de 6 caras
# Usar una lista de comprensión para dibujar muchos números aleatorios
# Usar `sum` y una expresión generadora para contar valores.
# Convierte el siguiente código a una versión sin comprensiones.
# Lancemos un dado 100 mil veces
import random

# Método para generar los 100000 lanzamientos del dado
def generarLanzamientos():
    lanzamientos = []
    for i in range(100000):
        lanzamientos.append(random.randint(1, 6))
    return lanzamientos

# Metodo para calcular con que frecuencia aparece cada cara
def obtenerFrecuenciasCara(listaLanzamientos):
    # Recorremos todas las caras del dado
    for cara in range(1, 7):
        contador = 0
        # Recorremos cada uno de los lanzamientos
        for lanzamiento in listaLanzamientos:
            if lanzamiento == cara:
                contador += 1
        # Obtenemos el porcentaje de cada cara
        porcentaje = (contador / len(listaLanzamientos)) * 100
        print(f'- Cara {cara}: {contador} veces {porcentaje}%')

listaLanzamientos = generarLanzamientos()
obtenerFrecuenciasCara(listaLanzamientos)
