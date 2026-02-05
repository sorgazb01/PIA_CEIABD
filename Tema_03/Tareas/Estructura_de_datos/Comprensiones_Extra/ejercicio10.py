# 10. Transforma los siguientes códigos a comprensiones de lista.
# 1. Desempaqueta todos los números de la matriz 3D en una única lista
# 2. Desempaqueta todos los nombres de la matriz 2D para que estén todos capitalizados 
# (primera letra en mayúsculas)
# 3. Obten una lista solo con las letras que están en mayusculas.
# Resultados:
# [1, 2, 3, 4, 5]
# ['Alice', 'Adam', 'Abilio', 'Dylan', 'Diana']
# ['A', 'B', 'I', 'K', 'L', 'Ñ', 'O', 'Q', 'S', 'U', 'W', 'X', 'Y', 'Z']
# Soluciones:

matriz = [[[1, 2], [3, 4]], [[5]]]
grupoNombres = [['alIce', 'ADam', 'AbiliO'], ['Dylan', 'DiANa']]
letras = 'ABcdefghIjKLmnÑOpQrStUvWXYZ'

# Funcion para convertir la matriz 3D en una lista
def convertirMatrizALista(matriz):
    # Un bucle por cada dimension
    return [numero for matriz2D in matriz for lista in matriz2D for numero in lista]

# Funcion para poner los nombre capitalizados
def nombresCapitalizados(grupoNombres):
    # Convertimos los nombres capitalizados, primero recorremos la matriz y despues la lista generada
    return [nombre.capitalize() for listaNombres in grupoNombres for nombre in listaNombres]

# Funcion para obtener las mayusculas
def obtenerMayusculas(letras):
    # Recorremos la cadaena y almacenamos las letras en mayusculas
    return [letra for letra in letras if letra.isupper()]

print(convertirMatrizALista(matriz))
print(nombresCapitalizados(grupoNombres))
print(obtenerMayusculas(letras))