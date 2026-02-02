# Ejercicio 7 - Los números Glotones
# Implementar un programa que primero muestre en pantalla los números del 1 al 100, 
# a continuación mostrará de nuevo la misma lista de números pero sustituyendo los múltiplos
# de 3 por el palabra "ÑAM" y, a su vez, los múltiplos de 5 por "A_COMER". Para los números que, 
# al mismo tiempo, son múltiplos de 3 y 5, mostrar el mensaje "ÑAM_ÑAM_A_COMER".
# 
# Soluciona el problema con y sin comprensiones.

# Metodo para mostrar los numeros del 1 al 100
def mostrarNumeros1a100():
    print('Numeros del 1 al 100: ')
    for i in range(1,101):
        print(i, end= ' ')
    print(' ')

#a) Sin comprensiones

# Metodo para obtener los numeros glotones del 1 al 100 sin comprension
def mostrarNumerosGlotones():
    mostrarNumeros1a100()
    # Creamos una lista vacia que almacenara los numeros
    # glotones
    listaGlotones = []
    print('Lista numeros glotones: ')
    # Creamos un bucle que vaya del 1 al 100
    for numero in range(1,101):
        # Por cada numero comprobamos primero si es multiplo de 3 y de 5
        if numero % 3 == 0 and numero % 5 == 0:
            listaGlotones.append('ÑAM_ÑAM_A_COMER')
        # Si no lo es comprobamos que lo sea solo de 3
        elif numero % 3 == 0:
            listaGlotones.append('ÑAM')
        # Despues comprobamos que lo sea solo de 5
        elif numero % 5 == 0:
            listaGlotones.append('A_COMER')
        # Y si no cumple ninguna condicon lo añadimos normal
        else:
            listaGlotones.append(numero)
    return listaGlotones

print('Lista numeros glotones sin comprension: ')
print(mostrarNumerosGlotones())

#b) Con compresion

def generarNumerosGlotonesComprension():
    mostrarNumeros1a100()
    print('Lista numeros glotones: ')
    return ['ÑAM_ÑAM_A_COMER' if i % 3 == 0 and i % 5 == 0 else 'ÑAM' if i % 3 == 0 else 'A_COMER' if i % 5 == 0 else i for i in range(1, 101)]

print('Lista numeros glotones con comprension: ')
print(generarNumerosGlotonesComprension())