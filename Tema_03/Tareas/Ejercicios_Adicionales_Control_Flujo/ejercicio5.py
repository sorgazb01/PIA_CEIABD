# 5. Números Amigos

# Se dice que dos números son amigos si la suma de los divisores del primero de los números es igual a al segundo nº y la suma 
# de divisores del segundo número es igual al primero.
# Por ejemplo: 220 y 284 son números amigos

# 1. **Desarrolla un programa que nos permita saber si dos números son amigos.**

# 2. **Implementa una versión avanzada de tu programa para que te permita calcular los N primeros pares amigos.**

def sumaDivisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def sonNumerosAmigos(n1, n2):
    if sumaDivisores(n1) == n2 and sumaDivisores(n2) == n1:
        print(f'El numero {n1} y el numero {n2} son numeros amigos')
    else:
        print(f'El numero {n1} y el numero {n2} no son numeros amigos')

n1 = int(input('Introduce el numero 1: '))
n2 = int(input('Introduce el numero 2: '))

sonNumerosAmigos(n1, n2)
