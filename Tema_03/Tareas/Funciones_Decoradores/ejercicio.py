# 1.Implementar una función que calcule el promedio de una lista de números y utilizar un decorador para validar que la lista no esté vacía antes 
# de calcular el promedio.
# Tareas:
# 1. Definir una función `promedio(lista)` que calcule el promedio de una lista de números. La función debe devolver el promedio 
# como un valor de punto flotante.
# 2. Definir un decorador `validar_lista_no_vacia` que tome como parámetro la función promedio y valide que la lista de números
#  no esté vacía antes de llamar a la función promedio. Si la lista está vacía, el decorador debe lanzar una excepción 
# ValueError con el mensaje "La lista no puede estar vacía".
# 3. Aplicar el decorador `validar_lista_no_vacia` a la función `promedio` usando la notación @ y probar la función con 
# diferentes listas de números.

# Creamos la funcion decorador para validar si la lista
# esta vacia
def validar_lista_no_vacia(func):
    def wrapper(lista):
        # Comprobamos que la lista esta vacia
        if len(lista) == 0:
            # Devolvemos un mensaje de error
            raise ValueError('La lista no puede estar vacía')
        
        # Sino llamamos a la funcion de promedio
        return func(lista)
    return wrapper

# Aplicamos el decorador
@validar_lista_no_vacia
# Funcion para obtener el promedio de la lista
def promedio(lista):
    return sum(lista)/len(lista)

# Probamos la funcion con dos casos
# Lista con elementos
lista1 = [1, 2, 3, 4, 5]
try:
    print(promedio(lista1))
except ValueError as error:
    print(f'Error: {error}')
# Lista vacia
lista2 = []
try:
    print(promedio(lista2))
except ValueError as error:
    print(f'Error: {error}')