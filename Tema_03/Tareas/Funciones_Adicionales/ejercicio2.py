# 2. Número Narcisista
# Un número narcisista es un número que es la suma de sus propios dígitos, 
# cada uno elevado a la potencia del número de dígitos. Crea una función 
# que nos diga si un número es narcisista o no
# 
# Por ejemplo:
# 153 (3 dígitos):
# 1 ^ 3 + 5 ^ 3 + 3 ^ 3 = 1 + 125 + 27 = 153
# 1634 (4 dígitos):
# 1 ^ 4 + 6 ^ 4 + 3 ^ 4 + 4 ^ 4 = 1 + 1296 + 81 + 256 = 1634
# 
# El reto:
# Tu código debe devolver verdadero o falso dependiendo de si el número dado 
# es un número narcisista en la base 10.
# No se requiere la comprobación de errores para cadenas de texto u otras 
# entradas no válidas, solo se pasarán enteros válidos a la función.

# Funcion para comprobar si un numero es narcisista o no
def esNumeroNarcisista(numero):
    # Obtenemos los digitos del numero pasando a string
    digitos = str(numero)
    # Obtenemos la potencia atraves de la longitud de los digitos
    potencia = len(digitos)
    suma = 0
    for digito in digitos:
        suma += pow(int(digito), potencia)
    # Comprobamos que la suma sea igual al numero1
    return suma == numero

numero = 153
print(f'Es el numero {numero} un numero narcisista? {esNumeroNarcisista(numero)}')
