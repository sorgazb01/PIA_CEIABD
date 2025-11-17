# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

tabla = []
for index_fila in range(1,6):
    fila = []
    for index_col in range(1,6):
        fila.append(int(input(f"Introduce el numero de la fila {index_fila} y columna {index_col}")))
    tabla.append(fila)
    
print("Suma de los valores de las filas: ")
index_fila = 1
for fila in tabla:
    print(f"La suma de los elementos de la fila {index_fila} es {sum(fila)}")
    index_fila += 1
    
print("Suma de los valores de las columnas: ")
for index_col in range(1,6):
    suma = 0
    for fila in tabla:
        suma = suma + fila[index_col - 1]
    print(f"La suma de los elementos de la columna {index_col} es de {sum}")