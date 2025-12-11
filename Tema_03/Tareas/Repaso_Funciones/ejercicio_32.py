# 32. Generar una lista de números primos hasta N.
# Escribe una función que devuelva una lista de números primos hasta un número
# dado utilizando el método de la Criba de Eratóstenes.

def primosLimite(limite):
    # Primero comprobamos que el limite que pasa el usuario es menor que 2
    # no hay primos menores de 2
    if limite < 2:
        return []
    # En el caso de que el limite sea 2, es el unico numero primo dentro del limite
    if limite == 2:
        return [2]
    # Si no se cumple lo anterior
    # Primero calculamos el indice máximo que habrá de numeros primos
    # que es la mitad entera del limite - 1
    indiceMaximo = (limite - 1) // 2
    
    # Creamo un array booleano cuya longitud es el indice máximo,
    # lo creamos por defecto a true
    esPrimo = [True] * (indiceMaximo + 1)
    
    
    for i in range(int(pow(limite, 0.5) // 2)):
        if esPrimo[i]:
            numero = i * 2 + 3
            esPrimo[i + numero::numero] = [False] * ((indiceMaximo - (i + numero)) // numero + 1)
            
    return [2] + [i * 2 + 3 for i in range(indiceMaximo + 1) if esPrimo[i]]