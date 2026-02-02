# Ejercicio 6 - Eliminando primera aparición
# Escribe un programa en python que elimine la primera aparición de un elemento introducido por el usuario.
# Antes de eliminarlo comprueba si realmente existe en el array.
# 
# array1 = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# valor a eliminar = 3
# 
# array2 = array('i', [1, 5, 3, 7, 1, 9, 3])
# valor a eliminar = 1
# 
# array3 = array('i', [1, 5, 3, 7, 1, 9, 3])
# valor a eliminar = 8
from array import array

# Ejemplos de arrays
array1 = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
array2 = array('i', [1, 5, 3, 7, 1, 9, 3])
array3 = array('i', [1, 5, 3, 7, 1, 9, 3])

# Metodo para pedir al usuario que valor desea eliminar de un array
def pedirValorEliminar():
    valorEliminar = int(input("Introduce que valor vas a eliminar del array: "))
    return valorEliminar

# Metodo para eliminar todas las apariciones de un valor en un array
def eliminarValor(array, valorEliminar):
    # Primero comprobamos que el valor este en el array
    if valorEliminar in array:
        # Recorremos el array elemento a elemento
        for elemento in array:
            # Si ese elemento es igual al elemento a eliminar
            if elemento == valorEliminar:
                # Lo eliminamos
                array.remove(elemento)
    # Si no existe el valor en el array se lo indicamos al usuario
    else:
        print(f'El numero {valorEliminar} no se encuentra en el array.') 
        
# Probamos el metodo con cada uno de los arrays de ejemplo
# Y mostramos el array que queda despues del borrado
eliminarValor(array1, pedirValorEliminar())
print(f'Array 1 postborrado: {array1}')
eliminarValor(array2, pedirValorEliminar())
print(f'Array 2 postborrado: {array2}')
eliminarValor(array3, pedirValorEliminar())
print(f'Array 3 postborrado: {array3}')
