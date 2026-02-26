# Ejercicio 6 - Contador
# En este ejercicio deberás crear una función que realice varias tareas sobre un 
# fichero llamado contador.txt que almacenará un contador de visitas (será un número):
# Nuestro script trabajará sobre el fichero contador.txt. 
# Si el fichero no existe o está vacío lo crearemos con el número 0. 
# Si existe simplemente leeremos el valor del contador.
# Luego a partir de un argumento:
# 1. Si se envía el argumento inc, se incrementará el contador en uno y se mostrará 
# por pantalla.
# 2. Si se envía el argumento dec, se decrementará el contador en uno y se mostrará 
# por pantalla.
# 3. Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará 
# el valor del contador por pantalla.
# Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.
# Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error: 
# Fichero corrupto.

# Fichero contador
ficheroContador = 'contador.txt'

# Funcion para leer el valor de contador del fichero
def leerFicheroContador():
    try:
        # Abrimos el fichero en modo lectura
        with open(ficheroContador, 'r') as fichero:
            # Obtenemos el valor del contador eliminando espacios en blanco
            # para evitar errores al convertir a tipo entero
            contenido = fichero.read().strip()
            # Si el fichero esta vacio inicamos el contador a 0
            if not contenido:
                return 0
            # Sino devolvemos el valor del contador converitido a entero
            else:
                return int(contenido)
    # Si el fichero no existe devolvemos contador a 0
    except FileNotFoundError:
        return 0
    # Excepcion para manejar errores
    except ValueError:
        raise ValueError('Error. Fichero corrupto')

# Funcion para guardar el valor del contador en el fichero
def guardarValorContador(valor):
    # Abrimos el fichero en modo escritura
    with open(ficheroContador, 'w') as fichero:
        # Escribimos el valor de contador en el fichero
        fichero.write(str(valor))

# Funcion para ejecutar el contador
def contador(argumento):
    try:
        # Obtenemos el valor del contador del fichero
        valor = leerFicheroContador()
        # Si tiene arguemnto ejectuamos la accion correspondiente
        if argumento == 'inc':
            valor += 1
            print(f'Contador incrementado: {valor}')
        elif argumento == 'dec':
            valor -= 1
            print(f'Contador decrementado: {valor}')
        # Sino devolvemos el valor del contador por pantalla
        else:
            print(f'Valor del contador: {valor}')
        # Guardamos el valor actualizado del contador nuevo en el fichero
        guardarValorContador(valor)
    except ValueError as error:
        print(f"Error: {error}")

contador('')
contador('inc')
contador('dec')
contador('dec')
contador('')