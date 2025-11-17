# Crea una función “calcularMaxMin” que recibe una lista con valores 
# numéricos y devuelve el valor máximo y el mínimo. Crea un programa 
# que pida números por teclado y muestre el máximo y el mínimo, 
# utilizando la función anterior.ç
import random

def calcularMaxMin(lista):
    print(f'Valor máximo de la lista: {max(lista)}')
    print(f'Valor mínimo de la lista: {min(lista)}')
    
lista_numeros = []
for i in range(10):
    lista_numeros.append(random.randint(1,1000))
    
calcularMaxMin(lista_numeros)