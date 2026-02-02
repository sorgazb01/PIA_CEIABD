# Ejercicio 4 - Divisores de X
# Crea un programa que pida al usuario un número comprendido entre el 1 el 300 y genere una lista
# con todos los valores divisores.
# Resuelvelo sin y con comprensiones.

def pedirNumero1a300():
    while True:
        numero = int(input('Introduce un numero entre 1 y 300: '))
        if 1 <= numero <= 300:
            return numero
        else:
            print('Error. Numero fuera del rango. ')
            
numero = pedirNumero1a300()

#a)
def obtenerDivisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
        
print(f'La funcion sin compresion, devuelve los siguientes divisores para {numero}: {obtenerDivisores(numero)}')

#b)
def obtenerDivisoresCompresion(numero):
    return [i for i in range(1, numero + 1) if numero % i == 0]

print(f'La funcion con compresion, devuelve los siguientes divisores para {numero}: {obtenerDivisoresCompresion(numero)}')