# Ejercicio 12. Conservar Registros con N Apariciones del valor K
# Queremos conservar aquellos registros cuyo valor K esté N veces.
# Entrada : 
# lista_prueba = [[4, 5, 5, 4],[5, 4, 3]]
# K = 5
# N = 2
# Salida :
# [[4, 5, 5, 4]]
# Entrada : 
# lista_prueba = [[4, 5, 5, 4],[5, 4, 3]]
# K = 5
# N = 3
# Salida :
# []

# Función que conserva los registros cuyo valor sea K y aparezca N veces en la lista
def conservarRegistros (lista, k, n):
    resultao = []
    for fila in lista:
        if fila.count(k) == n:
            resultao.append(fila)
    return resultao

listaDeListas = [[4, 5, 5, 4],[5, 4, 3]]
k = 5
n = 2

print(f'Salida: {conservarRegistros(listaDeListas, k, n)}')