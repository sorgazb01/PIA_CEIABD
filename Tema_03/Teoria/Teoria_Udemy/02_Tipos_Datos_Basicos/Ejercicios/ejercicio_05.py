# Pedir el nombre y los dos apellidos de una persona
# y mostrar las iniciales.
nombre = input("Introduce un nombre: ")
apellido1 = input("Introduce el primer apellido: ")
apellido2 = input("Introduce el segundo apellido: ")

iniciales = nombre[0] + apellido1[0] + apellido2[0]

print("Las iniciales son: ", iniciales.upper())