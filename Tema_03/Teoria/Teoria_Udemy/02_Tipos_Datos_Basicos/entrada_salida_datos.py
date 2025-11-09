# Entrada y salida de datos en Python
nombre = input('Dime tu nombre: ')
print(type(nombre))
print(nombre)

num = int(input('Dame un entero: '))
print(type(num))
print(num)

num = float(input('Dame un número real: '))
print(type(num))
print(num)

print("Hola son las", 6, "de la tarde.")
print("Hola son las " + str(6) + " de la tarde.")

print("El producto %s cantidad = %d precio = %.2f"%("cesta", 23, 13.456))