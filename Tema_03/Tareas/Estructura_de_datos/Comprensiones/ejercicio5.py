# Ejercicio 5 - Generador de tuplas
# Dada una tupla de 4 elementos. Genera una lista de tuplas de 3 elementos combinando los 4 elementos de la tupla original.
# Hazlo usando comprension y sin ella.
# Ejemplo de Salida:
# [(3, 3, 3), (3, 3, 5), (3, 3, 7), (3, 3, 11), 
# (3, 5, 3), (3, 5, 5), (3, 5, 7), (3, 5, 11), 
# (3, 7, 3), (3, 7, 5), (3, 7, 7), (3, 7, 11), 
# (3, 11, 3), (3, 11, 5), (3, 11, 7), (3, 11, 11), 
# (5, 3, 3), (5, 3, 5), (5, 3, 7), (5, 3, 11), 
# (5, 5, 3), (5, 5, 5), (5, 5, 7), (5, 5, 11), 
# (5, 7, 3), (5, 7, 5), (5, 7, 7), (5, 7, 11), 
# (5, 11, 3), (5, 11, 5), (5, 11, 7), (5, 11, 11), 
# (7, 3, 3), (7, 3, 5), (7, 3, 7), (7, 3, 11), 
# (7, 5, 3), (7, 5, 5), (7, 5, 7), (7, 5, 11), (7, 7, 3), 
# (7, 7, 5), (7, 7, 7), (7, 7, 11), (7, 11, 3), (7, 11, 5), 
# (7, 11, 7), (7, 11, 11), (11, 3, 3), (11, 3, 5), (11, 3, 7),
# (11, 3, 11), (11, 5, 3), (11, 5, 5), (11, 5, 7), (11, 5, 11), 
# (11, 7, 3), (11, 7, 5), (11, 7, 7), (11, 7, 11), (11, 11, 3), 
# (11, 11, 5), (11, 11, 7), (11, 11, 11)]

# Ejemplo de tupla de prueba
tupla = (3, 5, 7, 11)

#a) Con compresion

# Metod para generar la lista de tuplas usando una comprension 
# con bucles anidados
def generarTuplasCompresion(tupla):
    return [(a, b, c) for a in tupla for b in tupla for c in tupla]

print('Tuplas con compresion: ')
print(generarTuplasCompresion(tupla))

#b) Sin compresion

# Metodo para generar la lista de tuplas sin usar una comprension
def generarTuplas(tupla):
    listaTuplas = []
    for a in tupla:
        for b in tupla:
            for c in tupla:
                listaTuplas.append((a, b, c))
    return listaTuplas

print('Tuplas sin comprension: ')
print(generarTuplas(tupla))