cadena = 'hola, cómo estás?'
print(cadena)

print(cadena.capitalize())

cad = 'Hola Mundo'
print(cad)
print(cad.upper())
print(cad.lower())
print(cad.swapcase())
print(cad.title())

cad = 'bienvenido a mi aplicacion'

print(cad.count('a'))
print(cad.count('a',16))
print(cad.count('a',10,16))
print(cad.find('mi'))
print(cad.find('hola'))
print(cad.startswith('b'))
print(cad.startswith('bien'))
print(cad.startswith('bien',13))
print(cad.endswith('cion'))
print(cad.replace('a', 'U'))

cadena = "   www.eugeniabahit.com   "
print(cadena)
print(cadena.strip())

cadena = "000000123000000"
print(cadena.strip("0"))

hora = "12:23:12"
print(hora.split(":"))

texto = "Linea 1\nLinea 2\nLinea 3"
print(texto)
print(texto.splitlines())