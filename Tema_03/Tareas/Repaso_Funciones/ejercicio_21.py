# 21. Convertir un número binario a decimal.
# Escribe una función que convierta un número binario en su equivalente 
# decimal.

def convertirADecimal(numeroBinario):
    numeroDecimal = 0
    lenNumeroBinario = len(numeroBinario)
    for i in range(lenNumeroBinario):
        cifraBinaria = int(numeroBinario[lenNumeroBinario - 1 -i])
        numeroDecimal = numeroDecimal + cifraBinaria * pow(2, i)
    return numeroDecimal

numeroBinario = input("Introduce un numero binario: ")
print(f'Su numero decimal es: {convertirADecimal(numeroBinario)}')