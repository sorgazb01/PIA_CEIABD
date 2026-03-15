import cadenas

def main():
    texto = input("Introduce una cadena de texto: ")

    print(f"Cadena invertida: {cadenas.invertir(texto)}")
    print(f"Número de vocales: {cadenas.contar_vocales(texto)}")
    print(f"En mayúsculas: {cadenas.a_mayusculas(texto)}")
    print(f"En minúsculas: {cadenas.a_minusculas(texto)}")

main()