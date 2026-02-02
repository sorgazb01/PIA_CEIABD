# Ejercicio 4 - Divisores de X
# Crea un programa que pida al usuario un número comprendido entre el 1 el 300 y genere una lista
# con todos los valores divisores.
# Resuelvelo sin y con comprensiones.

# Metodo para pedir al usuario un numero entre 1 y 300
def pedirNumero1a300():
    # Bucle infinito hasta que el usuario introduzca un numero validp
    while True:
        numero = int(input('Introduce un numero entre 1 y 300: '))
        if 1 <= numero <= 300:
            return numero
        else:
            print('Error. Numero fuera del rango. ')
            
numero = pedirNumero1a300()

#a)

# Metodo para obtener los divisores de un numero sin comprensiones
def obtenerDivisores(numero):
    # Lista de divisores
    divisores = []
    # Creamos un bluce desde el 1 hasta el numero incluido
    for i in range(1, numero + 1):
        # Comprobamos si el numero es divisible
        if numero % i == 0:
            # Y lo añadimos a la lista de divisores
            divisores.append(i)
    # Devolvemos la lista
    return divisores
        
print(f'La funcion sin compresion, devuelve los siguientes divisores para {numero}: {obtenerDivisores(numero)}')

#b)

# Metodo para obtener los divisores de un numero con compresiones
def obtenerDivisoresCompresion(numero):
    # Creamos la lista con compresion con el mismo bucle y condicion del metodo antetior
    return [i for i in range(1, numero + 1) if numero % i == 0]

print(f'La funcion con compresion, devuelve los siguientes divisores para {numero}: {obtenerDivisoresCompresion(numero)}')