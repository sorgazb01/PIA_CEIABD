# Ejercicio 4. Valores.
# lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
# ¿Sabrías hacer que Python te diga cuántas repeticiones del valor 10 hay en esta lista?

lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]

# Función que cuenta cuántas veces aparece un número en una lista
def contarNumerosRepetidos(lista, numero):
    contador = 0
    for elemento in lista:
        if elemento == numero:
            contador += 1
    return contador

numero = 10
vecesRepetido = contarNumerosRepetidos(lista_numeros, numero)

print(f'El número {numero} aparece {vecesRepetido} veces en la lista.')