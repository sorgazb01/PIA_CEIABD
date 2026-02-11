# Ejercicio 7 - Una Morsa con Mapa y Diccionario...
# En el siguiente ejercicio vamos a repasar el uso de maps, operador morsa (:=) y 
# diccionarios.

# Dado el diccionario de datos dic:
# lista1 = [-3, -6, -9, -12, -15]
# Lista2 = [-18, 15, 12, 9, 6, 3]
# Lista3 = [2, 3, 4, 5, 6, 7, 8]
# dic = {1:lista1,
#        2:lista2,
#        3:lista3      
#       }
# La función funcionX recibe por parametro un valor(x) y devuelve un número decimal.
# Las operaciones que realizan son las siguientes:
# 
# Si x > 1:
# resultado = función exp(x)/x-1
# Si x < 1
# resultado = función exp(x)/(x-1)<sup>2</sup>
# Si x = 1:
# resultado = 0
# 
# Implementa una función que aplique la función funcionX a todos los valores del 
# diccionario y se quede con aquellos resultados superiores a 0.5. 
# a) El resultado debe aparecer en una única lista.     
# b) El resultado aparezca dividido por cada lista del diccionario.
# 
# Solución:
import math

# Datos problema
lista1 = [-3, -6, -9, -12, -15]
lista2 = [-18, 15, 12, 9, 6, 3]
lista3 = [2, 3, 4, 5, 6, 7, 8]
dic = {1: lista1, 2: lista2, 3: lista3}

# FuncionX
def funcionX(x):
    if x > 1:
        return math.exp(x)/(x - 1)
    elif x < 1:
        return math.exp(x)/pow((x - 1), 2)
    else:
        return 0
    
# Soluciones

# Para el apartado A usamos una comporesion que devolvera una lista con todos
# los valors del diccionario, primero recorremos las lista del diccionario,
# despues cada numero de cada lista y vamos devolviendo el resultado si la funcionX
# devuelve un numero mayor a 0.5
apartadoA = [resultado for lista in dic.values() for numero in lista if (resultado := funcionX(numero)) > 0.5]    

# Para el aparado B usamos otra compresion que en ese caso devuelve un diccionario, en el que 
# mostramos primero el numero de la lista en el que estamos, y sus valores seran los resultados
# obtenidos de aplicar la funcionX a cada valor de la lista correspondiente en caso de que sea mayor a
# 0.5
apartadoB = { numeroLista : [resultado for numero in lista if (resultado := funcionX(numero)) > 0.5] 
             for numeroLista, lista in dic.items()}

# Mostramos la solucion a cada apartado
print(f'Solucion apartado A: {apartadoA}')
print(f'Solucion apartado B: {apartadoB}')