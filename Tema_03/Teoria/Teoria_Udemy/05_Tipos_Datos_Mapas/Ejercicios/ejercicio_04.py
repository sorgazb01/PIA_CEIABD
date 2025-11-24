#Ejercicio 5
#Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono.
# El programa nos dará el siguiente menú:
#Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
# opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar 
# el teléfono correspondiente.
#Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
#Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
#Listar: Nos muestra todos los contactos de la agenda.
#Implementar el programa con un diccionario.

agenda = {}

while True:
    print('1 - Añadir/Modificar contacto.')
    print('2 - Buscar contacto.')
    print('3 - Borrar contacto.')
    print('4 - Mostrar todos los contactos.')
    print('0 - Salir.')
    opcion = input('Introduce una opción: ')
    if opcion == '1':
        nombre_contacto = input('Introduce el nombre del contacto: ')
        if nombre_contacto in agenda:
            print(f'Contacto: {nombre_contacto} -> Teléfono: {agenda[nombre_contacto]}')
            cambiar_telefono = input(f'¿Quieres modificar el teléfono de {nombre_contacto}? (S/n):')
            if cambiar_telefono.lower() == 's':
                nuevo_telefono = input('Introduce el nuevo número de teléfono: ')
                agenda[nombre_contacto] = nuevo_telefono
        else:
            telefono = input(f'Introduce el número de teléfono para {nombre_contacto}: ')
            agenda[nombre_contacto] = telefono
    elif opcion == '2':
        cadena = input('Introduce un nombre: ')
        for nombre in agenda:
            if nombre.startswith(cadena):
                print(f'Contacto: {nombre} -> Teléfono: {agenda[nombre]}')
    elif opcion == '3':
        nombre_borrar = input('Introduce el nombre del contacto a borrar: ')
        if nombre_borrar in agenda:
            borrar = input(f'¿Deseas borrar el contacto de {nombre_borrar}? (S/n):')
            if borrar.lower() == 's':
                del agenda[nombre_borrar]
                print(f'Contacto {nombre_borrar} borrado.')
    elif opcion == '4':
        for nombre, telefono in agenda.items():
            print(f'Contacto: {nombre} -> Teléfono: {telefono}')
    elif opcion == '0':
        print('Saliendo...')
        break
    else:
        print('Error. Has introducido una opción no válida.')