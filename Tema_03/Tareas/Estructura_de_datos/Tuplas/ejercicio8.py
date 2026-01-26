### Ejercicio 8
# Dadas dos tuplas:
# a) Crear una lista con todas las combinaciones que se pueden dar entre los elementos de las dos tuplas(pueden incluir repetidos)
# b) ¿Y sin repetidos?
# Ejemplos:
# **Entrada : tupla1 =(7, 2), tupla2 =(7, 8)**
# **Salida : [(7, 7),(7, 8),(2, 7),(2, 8),(7, 7),(7, 2),(8, 7),(8, 2)]**
#### Solución:


tupla1 = (7,2)
tupla2 = (7,8)

lista_combinaciones = []

for elemento_tupla1 in tupla1:
    for elemento_tupla2 in tupla2:
        combinacion = (elemento_tupla1, elemento_tupla2)
        lista_combinaciones.append(combinacion)
        
for elemento_tupla2 in tupla2:
    for elemento_tupla1 in tupla1:
        combinacion = (elemento_tupla2, elemento_tupla1)
        lista_combinaciones.append(combinacion)
        
print(lista_combinaciones)

print('Sin repetidos: ')
lista_sin_repetidos = []
for elemento in lista_combinaciones:
    if elemento not in lista_sin_repetidos:
        lista_sin_repetidos.append(elemento)
print(lista_sin_repetidos)
