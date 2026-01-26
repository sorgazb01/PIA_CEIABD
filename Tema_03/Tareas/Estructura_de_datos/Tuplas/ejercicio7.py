# Ejercicio 7
# Modifica el ejercicio 6 para crear una lista de tuplas donde, aparezcan el divisor,el dividendo, la operación (%) 
# y el resultado.
# Ejemplo:
# lista_resultado = [(10, 5, '%', 0), (4, 6, '%', 4), (5, 7, '%', 5), (6, 5, '%', 1)]

# Tuplas ejemplos
tupla1 = (10, 4, 5, 6)
tupla2 = (5, 6, 7, 5)

# Funcion para generar lista de tuplas de los modulos
def tuplaModulos(tupla1, tupla2):
    lista_resultado = []
    # Creamos una lista mezclando cada elemento de las tuplas
    tupla_zip = zip(tupla1, tupla2)
    for elemento in tupla_zip:
        # Obtenemos cada parte de la operacion
        divisor = elemento[0]
        dividendo = elemento[1]
        operando = '%'
        resultado = divisor % dividendo
        # Creamos la tupla de la operacion
        tupla_resultado = (divisor, dividendo, operando, resultado)
        # La añadimos a la lista
        lista_resultado.append(tupla_resultado)
    return lista_resultado

print(tuplaModulos(tupla1, tupla2))