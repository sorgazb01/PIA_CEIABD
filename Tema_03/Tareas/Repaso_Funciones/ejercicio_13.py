# 13. Contar cuántas veces aparece una subcadena en una cadena.
# Implementa una función que cuente las veces que una subcadena 
# aparece dentro de una cadena.

def contadorSubcadena(cadena, subcadena):
    contador = 0
    for palabra in cadena.split():
        if subcadena in palabra:
            contador = contador + 1
    return contador

cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena para buscar:")

resultado = contadorSubcadena(cadena, subcadena)
print(f"La subcadena {subcadena} aparece {resultado} veces")