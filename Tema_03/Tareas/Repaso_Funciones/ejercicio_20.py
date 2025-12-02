# 20. Generar un número aleatorio entre un rango dado.
# Crea una función que genere un número aleatorio entre un mínimo y un máximo
# dados.
import random

def numeroRandomRango(lim_minimo, lim_maximo):
    numeroRandom = random.randint(lim_minimo, lim_maximo)
    return numeroRandom

lim_minimo = int(input("Introduce el limite minimo: "))
lim_maximo = int(input("Introduce el limite maximo: "))

numeroRandomLimite = numeroRandomRango(lim_minimo, lim_maximo)

print(f"El numero aleatiorio entre {lim_minimo} y {lim_maximo} es: {numeroRandomLimite}")