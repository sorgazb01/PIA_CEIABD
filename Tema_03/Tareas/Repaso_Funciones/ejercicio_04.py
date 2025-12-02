# 4. Verificar si un número es primo.
# Crea una función que reciba un número y devuelva si es primo o no.

def esPrimo(numero):
    if numero <= 1:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
                break
            else:
                return True
            
numero = int(input('Introduce un numero: '))
if esPrimo(numero):
    print(f'El numero {numero} es Primo')
else:
    print(f'El numero {numero} no es Primo')
