# Problema 2. Frecuencia de palabras en un texto.
# Escribe un programa que pida al usuario ingresar una frase o párrafo. Luego, el
# programa debe contar cuántas veces aparece cada palabra en el texto y
# mostrar las palabras junto con su frecuencia.
# Requisitos:
# 1. Eliminar los signos de puntuación y convertir todas las palabras a
# minúsculas para evitar diferencias.
# 2. Usar un diccionario donde la clave sea la palabra y el valor sea su
# frecuencia.
# 3. Mostrar las palabras y sus frecuencias de forma ordenada por la
# palabra.

def contar_palabras(texto):
    texto = texto.split()

    lista_palabras = []
    
    for palabra in texto:
        palabra = palabra.strip('.,;:!?"()[]{}').lower()
        lista_palabras.append(palabra)

    diccionario = {}
    for palabra in lista_palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    print("Palabra - Frecuencia")
    for palabra in sorted(diccionario.keys()):
        print(palabra, diccionario[palabra])


texto = input("Ingresa una frase o parrafo: ")
contar_palabras(texto)