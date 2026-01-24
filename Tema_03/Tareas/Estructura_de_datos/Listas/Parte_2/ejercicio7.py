# Ejercicio 7. Frecuencia mayor que K
# Extrae los elementos de la lista L cuya frecuencia es mayor que K. Siendo K un valor introducido por el usuario.
# L = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

L = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

# Función que se encarga de pedir al usuario el valor de k
def pedirK():
    k = int(input('Introduce un valor para K: '))
    return k

# Funciíon que devuelve la lista de elementos cuya frecuencia en la lista es mayor que k
def frecuenciaMayorK(lista, k):
    mayoresK = []
    for elemento in lista:
        # Cuenta las veces que aparece en la lista y si es mayor que k y no está en la lista
        # de mayores que k lo añade
        if lista.count(elemento) > k and elemento not in mayoresK:
            mayoresK.append(elemento)
    return mayoresK

# Función que muestra el resultado del ejercicio
def resultado(lista,k):
    if len(lista) == 0:
        print(f'No hay elementos con una frecuencia superior a {k}')
    else:
        print(f'Los elemnentos con una frecuencia superior a {k} son: {lista}')

k = pedirK()
mayoresK = frecuenciaMayorK(L, k)

resultado(mayoresK, k)