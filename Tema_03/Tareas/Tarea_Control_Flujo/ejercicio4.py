# Ejercicio 4

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M o los hombres con un nombre 
# posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y 
# muestre por pantalla el grupo que le corresponde.

nombre = input('Introduce un nombre: ').capitalize()

while True:
    sexo = input('Introduce el sexo (H/M): ').upper()
    if sexo == 'H' or sexo == 'M':
        break
    else:
        print('Error al introducir el sexo')

primeraLetra = nombre[0]

if (sexo == 'M' and primeraLetra < 'M') or (sexo == 'H' and primeraLetra > 'N'):
    print('Perteneces al grupo A')
else:
    print('Perteneces al grupo B')