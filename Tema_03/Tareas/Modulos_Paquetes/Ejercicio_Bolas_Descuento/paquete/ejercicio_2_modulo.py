# Importamos la libreria random
import random

# Diccionario con las bolas y descuentos
descuentos = {
    "Blanca": 0,
    "Roja": 10,
    "Azul": 20,
    "Verde": 25,
    "Amarilla": 50,
}

# Funcion para elegir una bola al azar
def seleccionarBola():
    bolas = list(descuentos.keys())
    return random.choice(bolas)

# Funcion para obtener el descuento segun la bola seleccionada
def obtenerDescuento(bola):
    return descuentos[bola]

# Funcion para obtener el precio con descuento
def calcularTotal(totalCompra, porcentaje):
    descuento = totalCompra * porcentaje / 100
    return totalCompra - descuento

# Funcion para mostrar el resultado al usuario
def mostrarResultado(totalCompra, bola, porcentaje, nuevoTotal):
    print(f"Has sacado la bola: {bola}")
    if porcentaje == 0:
        print("Lo sentimos, no tienes descuento.")
        print(f"Total a pagar: {totalCompra:.2f}€")
    else:
        print(f"¡Enhorabuena! Tienes un {porcentaje}% de descuento.")
        print(f"Total a pagar: {nuevoTotal:.2f}€")