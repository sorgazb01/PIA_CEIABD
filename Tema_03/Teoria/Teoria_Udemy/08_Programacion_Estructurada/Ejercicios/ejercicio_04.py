# Ejercicio 4
# Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y 
# devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, 
# “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

def convertirEspaciado(texto):
    texto_espacios = ''
    for letra in texto:
        texto_espacios += letra + ' '
    return texto_espacios

texto = input('Introduce un texto: ')
print(convertirEspaciado(texto))