secreto = "asdasd"
clave = input("Introduce la clave: ")

while clave != secreto:
    print("Error. Clave incorrecta.")
    otra = input("¿Quieres introducir otra clave? (S/N): ")
    if otra.upper() == 'N':
        break
    clave = input("Introduce la clave: ")
if clave == secreto:
    print("Bienvenido !!!")
print("Programa terminado.")