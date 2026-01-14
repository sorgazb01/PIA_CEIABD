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


def paresNumerosAmigos(n):
    paresNumerosAmigos = []
    numero = 1
    numerosComprobados = set()

    while len(paresNumerosAmigos) < n:
        if numero not in numerosComprobados:
            suma = sumaDivisores(numero)
            if suma > numero and sumaDivisores(suma) == numero:
                paresNumerosAmigos.append((numero, suma))
                numerosComprobados.add(numero)
                numerosComprobados.add(suma)
        numero += 1
    
    return paresNumerosAmigos

rangoNumerosAmigos = int(input("Cuantos pares de numeros amigos quieres mostrar?: "))
pares = paresNumerosAmigos(rangoNumerosAmigos)
for par in pares:
    print(par)

