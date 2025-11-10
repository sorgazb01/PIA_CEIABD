# Escribe un programa que pida un nombre de usuario y una contraseña
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema"
# sino se da un error.

nombre_usuario = input("Introduce el nombre de usuario: ")
contrasenia = input("Introduce la contraseña: ")

if nombre_usuario =='pepe' and contrasenia == 'asdasd':
    print("Has entrado al sistema.")
else:
    print("Error, credenciales incorrectas.")