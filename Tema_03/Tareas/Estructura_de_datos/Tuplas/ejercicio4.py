### Ejercicio 4
# Dada una lista de números. Escribe un programa Python para crear una lista de tuplas que tenga el primer elemento como número y el segundo elemento como cubo del número.
# **Ejemplo de funcionamiento**
# Entrada: lista = [1, 2, 3]
# Salida: [(1, 1),(2, 8),(3, 27)]
# Entrada: lista = [9, 5, 6]
# Salida: [(9, 729),(5, 125),(6, 216)]
#### Solución:



lista = [1, 2, 3]

lista_tuplas = []

for numero in lista:
    tupla = (numero, pow(numero,3))
    lista_tuplas.append(tupla)
    
print(lista_tuplas)