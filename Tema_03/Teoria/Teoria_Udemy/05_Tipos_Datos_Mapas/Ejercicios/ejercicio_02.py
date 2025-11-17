# Vamos a crear un programa en python donde vamos a declarar un 
# diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que 
# se ha vendido y nos mostrará el precio final de la fruta a partir 
# de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el 
# programa nos preguntará si queremos hacer otra consulta.

diccionario_frutas = {'manzana': 5, 'platano': 2, 'kiwi': 10, 'mandarina': 5}

while True:
    nombre_fruta = input('Introduce el nombre de la fruta: ')
    if nombre_fruta not in diccionario_frutas:
        print('Error, esa fruta no se encuentra en el diccionario.')
    else:   
        cantidad = int(input('Introduce la cantidad de la fruta: '))
        print(f'Precio para la cantidad solicitada es: {cantidad * diccionario_frutas[nombre_fruta]}')
        
    otra_consulta = input('Deseas realizar otra consulta (S/n): ')
    if otra_consulta.lower() == 'n':
        break
    
