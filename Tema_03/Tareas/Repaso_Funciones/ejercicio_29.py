# 29. Verificar si un número es un número Armstrong.
# Crea una función que verifique si un número es un número Armstrong (por ejemplo,153).

def esNumeroArmstrong(numero):
    numeroString = str(numero)
    numeroCifras = len(numeroString)
    suma = 0
    for cifra in numeroString:
        suma += pow(int(cifra), numeroCifras)
    if suma == numero:
        print(f'El numero {numero} es un numero Armstrong')
    else:
        print(f'El numero {numero} no es un numero Armstrong')

numero = int(input('Introduce un numero: '))
esNumeroArmstrong(numero)