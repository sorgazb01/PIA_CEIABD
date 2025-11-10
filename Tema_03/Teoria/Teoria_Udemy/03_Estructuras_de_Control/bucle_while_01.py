secreto = 'asdasd'

while True:
    clave = input('Introduce la clave: ')
    if clave != secreto:
        print('Error. Clave incorrecta.')
    if clave == secreto:
        break
print('Bienvenido !!!')
print('Programa terminado.')