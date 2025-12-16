# Lista en la que se almcacenaran los libros
lista_libros = []
    
# Función que pide al usario el numero de libros que va a registrar, la infromación de cada
# uno de ellos y despues muestra la lista.
def leer_libros():
    # Pedimos al usuario el numero de libros a registrar
    numero_libros = int(input('Introudce el numero de libros a registrar: '))
    # pedimos los datos de cada uno de ellos y los almacenamos en un diccionario para
    # añadir ese diccionario a la lista de libros
    for item in range(numero_libros):
        titulo = input('Introduce el titulo del libro: ')
        autor = input('Introduce el autor del libro: ')
        anio_publicacion = int(input('Introduce el año de publicación del libro: '))
        leido = input('Introude si te has leido el libro o no: (S/n) ')
        print('')
        leido = leido.lower()
        if leido == 's':
            leido = 'Sí'
        else:
            leido = 'No'
        libro = {'Titulo': titulo, 'Autor': autor, 'Año Publicacion': anio_publicacion, 'Leido': leido}
        lista_libros.append(libro)
        
    # Recorremos la lista de libros, y de cada uno de sus diccionarios mostramos la clave valor (datos de los libros)
    print("--- LISTA DE LIBROS ---\n")
    for libro in lista_libros:
        print('--- LIBRO ---')
        for clave,valor in libro.items():
            print(f'{clave},{valor}')
        print('')
      
# Función que muestra por pantalla el numero de libros ledios y el numero de no leidos
def contar_libros_leidos(lista_libros):
    print(f"--- CONTADOR ESTADO LIBROS ---")
    # Variables contador
    libros_leidos = 0
    libros_sin_leer = 0
    # Recorremos la lista de libros
    for libro in lista_libros:
        # Recorremos la clave valor de cada diccionarios en busca de la clave
        # leido y compramos con sus dos posibles valores
        for clave,valor in libro.items():
            if clave == 'Leido' and valor == 'Sí':
                libros_leidos += 1
            elif clave == 'Leido' and valor == 'No':
                libros_sin_leer += 1
    # Mostramos el resultado final
    print(f'Total de libros leidos: {libros_leidos}')     
    print(f'Total de libros sin leer: {libros_sin_leer}')
    print('') 
    
# Funcion que muestra por pantalla el año medio de publicacion de los libros de la lista
def obtener_anio_medio(lista_libros):
    print(f"--- AÑO MEDIO PUBLICACION ---")
    # Sumador de años de publicacion
    suma_anios = 0
    # Recorremos la lista de libros
    for libro in lista_libros:
        # Recorremos la clave valor de cada diccionarios en busca de la clave
        # Año Publicacion y sumamos sus valores
        for clave, valor in libro.items():
            if clave == 'Año Publicacion':
                suma_anios += valor
    # Mostramos la media
    print(f'El año de publicación medio de todos los libros es: {round(suma_anios/len(lista_libros))}')
    print('')

# Función que recorre la lista en busca del autor solicitado
def buscar_libro_autor(autor, lista):
    print(f"--- LISTA DE LIBROS  DE {autor.upper()} ---")
    # Contador de libros del autos
    libros_autor = 0
    autor = autor.lower()
    # Recorremos la lista de libros
    for libro in lista:
        # Recorremos cada diccionario en busca de la clave Autor y el valor dado
        for clave, valor in libro.items():
            if clave == 'Autor' and valor.lower() == autor:
                libros_autor += 1
                # Mostramos solo la informacion necesaria
                print(f'Libro: {libro['Titulo']} {libro['Año Publicacion']}')
    # Si no hemos actualizado el contador mostramos que el autor no tiene libros
    if libros_autor == 0:
        print(f'El autor {autor} no existe o no tiene libros registrados.')
    print('')
    

# Funcion que muestra un resumen final
def resumen_final(lista_libros):
    print(f"---------- RESUMÉN LISTADO LIBROS ----------\n")
    # Devolvemos la longitud de la lista(numero de libros)
    numero_libros = len(lista_libros)
    print(f'El numero total de libros es: {numero_libros}')
    print('')
    contar_libros_leidos(lista_libros)
    obtener_anio_medio(lista_libros)
    autor = input('Introduce el nombre de un autor: ')
    buscar_libro_autor(autor, lista_libros)
    

leer_libros()
resumen_final(lista_libros)