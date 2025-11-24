# Ejercicio 4
# Codifica un programa en python que nos permita guardar 
# los nombres de los alumnos de una clase y las notas que 
# han obtenido. Cada alumno puede tener distinta cantidad de notas. 
# Guarda la información en un diccionario cuya claves serán los 
# nombres de los alumnos y los valores serán listas con las notas 
# de cada alumno.

# El programa pedirá el número de alumnos que vamos a introducir, 
# pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos 
# un número negativo. Al final el programa nos mostrará la lista de 
# alumnos y la nota media obtenida por cada uno de ellos. Nota: si se 
# introduce el nombre de un alumno que ya existe el programa nos dará 
# un error.
numero_alumnos = int(input('Introduce el número de alumnos que vas a registrar: '))

dic_alumnos = {}

for i in range(numero_alumnos):
    nombre_alumno = input(f'Introduce el nombre del alumno {i + 1}:')
    if nombre_alumno in dic_alumnos:
        print('Error. Ya existe ese alumno en el diccionario.')
    else:
        notas = []
        while True:
            nota = float(input(f'Introduce una nota para {nombre_alumno} (Introduce un número negativo para terminar): '))
            if nota < 0:
                break
            else:
                notas.append(nota)
        dic_alumnos[nombre_alumno] = notas
        
for alumno, notas in dic_alumnos.items():
    nota_media = sum(notas) / len(notas)
    print(f'Alumno: {alumno} -> Nota Media: {nota_media}')