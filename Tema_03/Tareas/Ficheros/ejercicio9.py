# Ejercicio 9 - Anagramas.
# Crea una serie de funciones para recibir un fichero de palabras (palabras.txt) 
# y devolver en un fichero denominado "lista_anagramas.txt" todos los anagramas de 
# cada una de las palabras. 
# La estructra de los ficheros será la siguiente:
# palabras.txt
# barca
# cordón
# usadme
# pasiva
# comas
# trapean
# grite
# 
# lista_anagramas.txt
# barca : [braca, cabra, carba]
# cordón : [cóndor]
# usadme : [mudase, medusa]
# 
# ¿Qué es un anagrama?
# Un anagrama es una palabra que resulta de la transposición de todas las letras de 
# otra palabra. Dicho de otra forma, una palabra es anagrama de otra si las dos tienen 
# las mismas letras, con el mismo número de apariciones, pero en un orden diferente.
# Por tanto para resolver este ejercicio, necesitaremos crear todas las combinaciones 
# (permutaciones) posibles de letras de cada palabra y comprobar si tienen sentido.
# Para comprobar el sentido de las palabras generadas, tenemos un diccionario con todas
# las palabras en castellano. Para cada permutación generada, comprobamos si existe en 
# el diccionario. En caso de existir, la almacenamos en el diccionario final de 
# soluciones.
# Los anagramas resultantes, no serán ni la palabra original, y deberán ser palabras 
# del castellano.
# Notas:
# 1. Se facilita el fichero diccionario_castellano.txt con todas las palabras del 
# castellano.

# Ficheros
ficheroEntrada     = 'palabras.txt'
ficheroDiccionario = 'diccionario_castellano.txt'
ficheroSalida      = 'lista_anagramas.txt'

# Metodo para obtener las palabras sin acentos y ordenadas alfabeticamente
def obtenerClave(palabra):
    # Pasamos a minúsculas y sustituimos cada vocal 'especial' por un valor normalizado
    palabra = palabra.lower()
    vocales = [('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'), ('ü', 'u'), ('ñ', 'n')]
    for caracterEspecial, normalizado in vocales:
        palabra = palabra.replace(caracterEspecial, normalizado)
    letras = []
    # Añadimos cada letra a la lista y la ordenamos alfabeticamente
    for letra in palabra:
        letras.append(letra)
    letras.sort()
    # Devolvemos una tupla que sera la clave del diccionario
    return tuple(letras)

# Metodo para cargar el diccionario de palabras agrupadas
def cargarDiccionario(ficheroDiccionario):
    diccionario = {}
    with open(ficheroDiccionario, encoding='utf-8') as fichero:
        lineas = fichero.readlines()
    for linea in lineas:
        palabra = linea.strip()
        # Ignoramos lineas vacias o compuestas
        if not palabra or ' ' in palabra:
            continue
        clave = obtenerClave(palabra)
        # Si la firma no existe la creamos con una lista vacia
        if clave not in diccionario:
            diccionario[clave] = []
        # Añadimos la palabra si no esta en la lista
        if palabra.lower() not in diccionario[clave]:
            diccionario[clave].append(palabra.lower())
    return diccionario

# Metodo para leer las palabras del fichero de entrada
def leerPalabras(ficheroEntrada):
    palabras = []
    with open(ficheroEntrada, encoding='utf-8') as fichero:
        lineas = fichero.readlines()
    for linea in lineas:
        if linea.strip():
            palabras.append(linea.strip())
    return palabras

# Metodo para encontrar los anagramas de cada palabra
def encontrarAnagramas(palabras, diccionarioPorClave):
    resultado = {}
    for palabra in palabras:
        clave = obtenerClave(palabra)
        # Obtenemos los candidatos con la misma clave
        if clave in diccionarioPorClave:
            candidatos = diccionarioPorClave[clave]
        else:
            candidatos = []
        # Filtramos la palabra original y ordenamos los anagramas
        anagramas = []
        for candidato in candidatos:
            if candidato.lower() != palabra.lower():
                anagramas.append(candidato)
        anagramas.sort()
        resultado[palabra] = anagramas
    return resultado

# Metodo para guardar el resultado en el fichero de salida
def guardarAnagramas(ficheroSalida, resultado):
    with open(ficheroSalida, 'w', encoding='utf-8') as fichero:
        for palabra, anagramas in resultado.items():
            fichero.write(f'{palabra} : {anagramas}\n')

diccionario = cargarDiccionario(ficheroDiccionario)
palabras = leerPalabras(ficheroEntrada)
resultado = encontrarAnagramas(palabras, diccionario)
guardarAnagramas(ficheroSalida, resultado)
