# Ejercicio 8.
# El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el 
# curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. 
# Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo 
# al final del curso (convocatoria ordinaria). Escribir un programa que contenga las 
# siguientes funciones:
# 
# 1. Una función que reciba el fichero de calificaciones y devuelva una lista de 
# diccionarios, donde cada diccionario contiene la información de los exámenes y 
# la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.
# 
# 2. Una función que reciba una lista de diccionarios como la que devuelve la función 
# anterior y añada a cada diccionario un nuevo par con la nota final del curso. 
# El peso de cada parcial de teoría en la nota final es de un 30% mientras que el 
# peso del examen de prácticas es de un 40%.
# 
# 3. Una función que reciba una lista de diccionarios como la que devuelve la función 
# anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos 
# suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 
# 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota 
# final mayor o igual que 5.

# Fichero de calificaciones
ficheroCalificaciones = 'calificaciones.csv'

# Metodo para convertir el sting a float
def obtenerNota(valor):
    # Si el valor es None o una cadena vacia devolvemos None
    if valor is None or valor.strip() == '':
        return None
    # Si no lo convertimos a float cambiando la coma por el punto decimal
    else:
        return float(valor.strip().replace(',', '.'))

# Metodo para leer el fichero de calificaciones
def leerFicheroCalificaciones(ficheroCalificaciones):
    # Lista de alumnos
    calificacionesAlumnos = []
    # Abrimos el fichero en modo lectura
    with open(ficheroCalificaciones, encoding="utf-8") as fichero:
        # Obtenemos las lienas del fichero
        lineas = fichero.readlines()
    # Ontenemos la cabecera del fichero separando los valores por ;
    cabecera = []
    for columna in lineas[0].split(';'):
        cabecera.append(columna.strip())
    # Recorremos las lineas del fichero a partir de la cabecera
    for linea in lineas[1:]:
        # Si la linea esta vacia pasamos a la siguiente
        if not linea.strip():
            continue
        # Si la linea no esta vacia separamos los valores por ;
        else:
            valores = linea.strip().split(';')
            # Creamos un diccionario con la cabecera y el valor de la columna
            fila = dict(zip(cabecera, valores))
            # Creamos un diccionario con los datos del alumno
            alumno = {
                'Apellidos':          fila['Apellidos'],
                'Nombre':             fila['Nombre'],
                'Asistencia':         int(fila['Asistencia'].replace('%', '')), # Convertimos el porcentaje a entero
                'Parcial1':           obtenerNota(fila['Parcial1']),
                'Parcial2':           obtenerNota(fila['Parcial2']),
                'Ordinario1':         obtenerNota(fila['Ordinario1']),
                'Ordinario2':         obtenerNota(fila['Ordinario2']),
                'Practicas':          obtenerNota(fila['Practicas']),
                'OrdinarioPracticas': obtenerNota(fila['OrdinarioPracticas']),
            }
            # Los añadimos a la lista de calificaciones de los alumnos
            calificacionesAlumnos.append(alumno)
    # Ordenamos la lista por apellidos
    calificacionesAlumnos.sort(key=lambda a: a["Apellidos"])
    return calificacionesAlumnos

# Metodo para calcular la nota final de cada alumno
def obtenerNotaFinal(alumnos):
    # Recorremos la lista de alumnos
    for alumno in alumnos:
        parcial1 = None
        parcial2 = None
        practicas = None
        # Obtenemos las notas de los examenes de cada alumno
        if alumno['Ordinario1'] is not None:
            parcial1 = alumno['Ordinario1']
        else:
            parcial1 = alumno['Parcial1']
        if alumno['Ordinario2'] is not None:
            parcial2 = alumno['Ordinario2']
        else:
            parcial2 = alumno['Parcial2']
        if alumno['OrdinarioPracticas'] is not None:
            practicas = alumno['OrdinarioPracticas']
        else:
            practicas = alumno['Practicas']
        # Si alguna de las notas es None, la nota final es None
        if parcial1 is None or parcial2 is None or practicas is None:
            alumno['NotaFinal'] = None
        # Sino calculamos la nota final redondendo a 2 decimales
        else:
            alumno['NotaFinal'] = round(parcial1 * 0.30 + parcial2 * 0.30 + practicas * 0.40, 2)
    return alumnos

# Metodo para clasificar los alumnos en aprobados y suspensos
def clasificacionAlumnos(alumnos):
    aprobados = []
    suspensos = []
    for alumno in alumnos:
        parcial1 = None
        parcial2 = None
        practicas = None
        notaFinal = None
        # Obtenemos las notas de los examenes de cada alumno
        if alumno['Ordinario1'] is not None:
            parcial1 = alumno['Ordinario1']
        else:
            parcial1 = alumno['Parcial1']
        if alumno['Ordinario2'] is not None:
            parcial2 = alumno['Ordinario2']
        else:
            parcial2 = alumno['Parcial2']
        if alumno['OrdinarioPracticas'] is not None:
            practicas = alumno['OrdinarioPracticas']
        else:
            practicas = alumno['Practicas']
        notaFinal = alumno['NotaFinal']
        # Comprobamos que alumno cumpla las condiciones para aprobar o no
        if (notaFinal is not None and notaFinal >= 5 and alumno['Asistencia'] >= 75 and parcial1 is not None and parcial1 >= 4 and parcial2 is not None and parcial2 >= 4 and practicas is not None and practicas >= 4):
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    # Mostramos los resultados
    print(f'Alumnos aprobados = {len(aprobados)}')
    for alumno in aprobados:
        print(f'- {alumno["Apellidos"]}, {alumno["Nombre"]}: {alumno["NotaFinal"]}')
    print(f'Alumnos suspensos = {len(suspensos)}')
    for alumno in suspensos:
        print(f'- {alumno["Apellidos"]}, {alumno["Nombre"]}: {alumno["NotaFinal"]}')

alumnos = leerFicheroCalificaciones(ficheroCalificaciones)
alumnos = obtenerNotaFinal(alumnos)
clasificacionAlumnos(alumnos)
