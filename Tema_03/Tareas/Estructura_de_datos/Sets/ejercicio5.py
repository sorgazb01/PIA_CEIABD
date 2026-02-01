# Ejercicio 5.
# Se nos dan una lista con n listas (matriz de listas) de cualquier tamaño que pueden tener elementos comunes.
# Necesitamos combinar todas estas matrices de tal manera que cada elemento deba aparecer solo una vez y los 
# elementos deben estar ordenados.
# Entrada:
# matriz = [
# [1, 2, 2, 4, 3, 6],
# [5, 1, 3, 4],
# [9, 5, 7, 1],
# [2, 4, 1, 3]]
# Salida:
# [1, 2, 3, 4, 5, 6, 7, 9]

matriz = [
    [1, 2, 2, 4, 3, 6],
    [5, 1, 3, 4],
    [9, 5, 7, 1],
    [2, 4, 1, 3]
]

# Metodo para convertir las matrices
def combinarMatrizListas(matriz):
    # Creamos un set vacio
    elementos = set()
    # Recorremos las listas de la matriz
    for lista in matriz:
        # Recorremos los elementos de la lista
        for elemento in lista:
            # Añadimos los elementos al set
            elementos.add(elemento)
    # Ordenamos el resultado
    resultado = sorted(elementos)
    return resultado

resultado = combinarMatrizListas(matriz)
print(resultado)