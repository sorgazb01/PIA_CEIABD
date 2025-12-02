# 21. Convertir un número binario a decimal.
# Escribe una función que convierta un número binario en su equivalente 
# decimal.

def convertirDecimal(numeroBinario):
    numeroBinarioString = str(numeroBinario)
    longitudNumeroBinario = len(numeroBinarioString)
    numeroDecimal = 0
    for i in range(longitudNumeroBinario):
        digitoBinario = int(numeroBinarioString[i])
        potencia = longitudNumeroBinario - i
        
