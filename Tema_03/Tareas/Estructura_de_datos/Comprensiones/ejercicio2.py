# Ejercicio 2 - El buscador de Aes.
# Dada una frase cualquiera, transforma cada palabra aplicando el siguiente criterio:
# Si la palabra contiene al menos una a la ponemos en mayuscula.
# Si la palabra NO contiene ninguna a irá con formato de título.
# a) Resuelve el problema sin comprensiones.
# b) Soluciona el ejercicio usando comprensión.

# Ejemplo frase de prueba
frase = 'En un lugar de La Mancha de cuyo nombre no quiero acordarme'

#a) Sin Compresiones

# Metodo para convertir la frase
def convertirFrase(frase):
    # Nueva variable que contendra la frase transformada
    nuevaFrase = ''
    # Recorremos la frase orignal palabra a palabra
    for palabra in frase.split():
        # Si la palabra contiene una A
        if 'a' in palabra.lower():
            # La ponemos en la nueva frase en mayusculas
            nuevaFrase += palabra.upper() + ' '
        else:
            # En caso contrario la ponemos en forma de titulo
            nuevaFrase += palabra.capitalize() + ' '
    # Devolvemos la nueva frase
    return nuevaFrase

print('Frase sin comprensiones: ')
print(convertirFrase(frase))

#b)

# Metodo para convertir la frase con comprensiones
def convertirFraseCompresion(frase):
    # Creamos la compresion con la condicion al principio y devolvemos la frase unida
    return ' '.join([palabra.upper() if 'a' in palabra.lower() else palabra.capitalize() for palabra in frase.split()])

print('Frase con comprensiones: ')
print(convertirFraseCompresion(frase))