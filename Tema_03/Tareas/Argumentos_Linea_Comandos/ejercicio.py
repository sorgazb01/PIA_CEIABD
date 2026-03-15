# Ejercicio 1 - Cifrado Vigenere
# Desarrolla un script que relize un cifrado o descifrado de Vigenere de un mensaje.
# El cifrado Vigenere consiste en utilizar una palabra como clave para cifrar el mensaje y 
# funciona de la siguiente forma:
# En nuestro alfabeto existen 27 letras. 
# Cada letra ocupa una posición. 
# Lo que hace el cifrado Vigenere es enfrentar las letras del mensaje a cifrar con la palabra clave.
# Por ejemplo:
# Mensaje a cifrar: PROGRAMACIONDEIA
# Palabra clave: COVID
# Ahora enfrentamos el mensaje a cifrar y la clave hasta que llegue al final del mensaje, 
# si se corta no pasa nada.
# PROGRAMACIONDEIA
# COVIDCOVIDCOVIDC
# Una vez las tenemos enfrentadas, sumamos la posición que ocupa cada letra enfrentada:
# p => 16
# C => 2
# Resultado = 18
# R => 18
# O => 15
# resultado = 33 
# Al resultado le hacemos el módulo con el total de letras del alfabeto y la posición resultante 
# será la letra con la que codificamos esa posición. Siguiendo con el ejemplo anterior
# 18 % 27 = 18 => le corresponderia la letra R
# 33 % 27 = 6  => le correspondería la letra G
# El script puede recibir 3 parámetros:
# -c seguido de una palabra para indicar que queremos cifrar esa palabra
# -d seguido de una palabra descifrar la palabra indicada.
# -k seguido de una palabra que funcionará como clave para el cifrado/descifrado
# No podemos cifrar y descifrar a la vez.
# Vamos a tener en cuenta solo las letras en mayúsculas y nuestros mensajes irán sin espacios 
# ni puntuaciones. Si en la terminal los mensajes se introducen en minúsculas, internamente lo 
# cambiaremos a mayúsculas.
# Ejemplo de uso:
# cifrar paralabra: python cifrado_vigenere.py -c PROGRAMACIONDEIA -k covid
# descifrado: python cifrado_vigenere.py -d RGKÑUCAVKLQBYMLC -k covid

 
# Importamos la libreria para trabajar con los argumentos en la linea de comando    
import argparse

# Alfabeto
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Metodo para cifrar un mensaje con una clave
def cifrar(mensaje, clave):
    mensaje = mensaje.upper()
    clave = clave.upper()
    # Variable que almacena el resultado del mensaje cifrado
    resultado = ""
    # Recorremos letra a letra el mensaje, obteniendo el indice de cada letra del mensaje de la clave
    for i, letra in enumerate(mensaje):
        posicionMensaje = alfabeto.index(letra)
        posicionClave = alfabeto.index(clave[i % len(clave)])
        # Aplicamos la formula de cifrado del cifrado Vigenere
        posicionCifrada = (posicionMensaje + posicionClave) % len(alfabeto)
        # Agregamos la letra cifrada al resultado
        resultado += alfabeto[posicionCifrada]
    return resultado

# Metodo para descifrar un mensaje con una clave
def descifrar(mensaje, clave):
    mensaje = mensaje.upper()
    clave = clave.upper()
    # Variable que almacena el resultado del mensaje descifrado
    resultado = ""
    # Recorremos letra a letra el mensaje, obteniendo el indice de cada letra del mensaje de la clave
    for i, letra in enumerate(mensaje):
        posicionMensaje = alfabeto.index(letra)
        posicionClave = alfabeto.index(clave[i % len(clave)])
        # Aplicamos la formula de descifrado del cifrado Vigenere
        posicionDescifrada = (posicionMensaje - posicionClave) % len(alfabeto)
        # Agregamos la letra descifrada al resultado
        resultado += alfabeto[posicionDescifrada]
    return resultado

# Metodo principal del programa
def main():
    # Creamos el parser para los argumento de la linea de comandos
    parser = argparse.ArgumentParser(description="Cifrado/Descifrado Vigenere")
    grupo = parser.add_mutually_exclusive_group()
    grupo.add_argument("-c", "--cifrar", help="Mensaje a cifrar")
    grupo.add_argument("-d", "--descifrar", help="Mensaje a descifrar")
    parser.add_argument("-k", "--key", required=True, help="Clave para el cifrado/descifrado")
    args = parser.parse_args()
    # Comprobamos los argumentos y realizamos el cifrado o el descifrado del mensaje
    if args.cifrar:
        resultado = cifrar(args.cifrar, args.key)
        print(f"Mensaje cifrado: {resultado}")
    elif args.descifrar:
        resultado = descifrar(args.descifrar, args.key)
        print(f"Mensaje descifrado: {resultado}")

main()       