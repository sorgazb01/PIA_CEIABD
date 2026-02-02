# Ejercicio 7. ¿Hay duplicados?
# Escribe un programa de Python para encontrar si un array de enteros contiene algún elemento duplicado.
# Devuelve verdadero si algún valor aparece al menos dos veces en dicha matriz y devuelve falso si cada 
# elemento es distinto. 
# 
# Ejemplos de salida:
# array1 = array('i', [1, 5, 3, 7, 1, 9, 3])
# Verdadero
# 
# array2 = array('i', [3, 7, 1, 9, 3])
# Verdadero
# 
# array3 = array('i', [5, 3, 7, 1, 9])
# Falso
from array import array

# Ejemplos de arrays
array1 = array('i', [1, 5, 3, 7, 1, 9, 3])
array2 = array('i', [3, 7, 1, 9, 3])
array3 = array('i', [5, 3, 7, 1, 9])

# Metodo que indica si hay elementos duplicados en un array
def hayDuplicados(array):
    # Creamos una lista que almacenara todos lo elementos duplicados
    # del array
    duplicados = []
    # Recorremos el array elemento a elemento
    for elemento in array:
        # Si el elemento aparece mas de una vez en el array
        if array.count(elemento) > 1:
            # Lo añadimos a la lista de duplicados
            duplicados.append(elemento)
    # Si la lista de duplicados tiene algun elemento
    if len(duplicados) > 0:
        # Devolvemos verdaderp
        return 'Verdadero'
    else:
        # Y falso en caso contrario
        return 'Falso'
        
# Probamos con cada uno de los arrays de ejemplo
print('Hay duplicados en el array1 ?: ' + str(hayDuplicados(array1)))
print('Hay duplicados en el array2 ?: ' + str(hayDuplicados(array2)))
print('Hay duplicados en el array3 ?: ' + str(hayDuplicados(array3)))