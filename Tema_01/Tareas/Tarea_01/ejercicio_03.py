# Problema 3. Intersección y unión de conjuntos
# Escribe un programa que permita al usuario crear dos conjuntos de números
# enteros. Luego, el programa debe calcular y mostrar:
# 1. La intersección de ambos conjuntos (elementos comunes).
# 2. La unión de ambos conjuntos (todos los elementos sin duplicados).
# 3. La diferencia simétrica (elementos que están en uno u otro conjunto,
# pero no en ambos).

def obtener_conjuntos(conjunto_1, conjunto_2):
    interseccion = conjunto_1.intersection(conjunto_2)
    print("La intersección de ambos conjuntos es:", interseccion)
    
    union = conjunto_1.union(conjunto_2)
    print("La unión de ambos conjuntos es:", union)
    
    diferencia_simetrica = conjunto_1.symmetric_difference(conjunto_2)
    print("La diferencia simétrica de los conjuntos es:", diferencia_simetrica)

# Solución con datos ya definidos

conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {3, 4, 5, 6, 7}

obtener_conjuntos(conjunto_1, conjunto_2)


# Solución solicitando los datos de los conjuntos al usuario

conjunto_aux_1 = set()
conjunto_aux_2 = set()

numeros_conjunto_1 = int(input("Numero de elementos del conjunto 1:"))

for numero in range(numeros_conjunto_1):
    numero = int(input("Numero " + str(numero+1) +":"))
    conjunto_aux_1.add(numero)
    
numeros_conjunto_2 = int(input("Numero de elementos del conjunto 2:"))

for numero in range(numeros_conjunto_2):
    numero = int(input("Numero " + str(numero+1) +":"))
    conjunto_aux_2.add(numero)

obtener_conjuntos(conjunto_aux_1, conjunto_aux_2)