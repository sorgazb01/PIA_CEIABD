# Ejercicio 4 Contar Palabras fichero internet.
# Escribir una función que acceda a un fichero de internet mediante su url y muestre 
# por pantalla el número de palabras que contiene. Si el fichero no existe, deberá 
# mostrar un mensaje informativo.
# 
# Nota: Podéis usar la página https://www.gutenberg.org/ donde hay libros en formato 
# de texto plano.

# Importaciones
from urllib import request
from urllib.error import URLError

# Funcion para contar las palabras de un libro URL
def contarPalabrasLibroURL(url):
    # Accedemos al fichero de internet mediante su URL
    # Si el fichero no existe se muestra un mensaje de error.
    try:
        with request.urlopen(url) as f:
            # Decodificamos el contenido a UTF-8 y lo separamos en palabras
            contenido = f.read().decode('utf-8')
            palabras = contenido.split()
            # Mostramos el numero de palabras del fichero URL
            print(f"El fichero contiene {len(palabras):,} palabras.")
    except URLError:
        print('¡La url ' + url + ' no existe!')

contarPalabrasLibroURL('https://www.gutenberg.org/cache/epub/1619/pg1619.txt')
        