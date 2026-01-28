# Ejercicio 3
# Dado un conjunto de palabras, determina si hay alguna palabra que tenga más de 10 caracteres. 
# Si hay al menos una palabra que tenga más de 10 caracteres, imprime la primera palabra encontrada 
# que cumpla con este criterio. Si no hay ninguna palabra que tenga más de 10 caracteres, imprime un 
# mensaje indicando que no se encontró ninguna palabra que cumpla con este criterio.

palabras = ['ordenador', 'mesa', 'frigorifico', 'coche']

for palabra in palabras:
    if len(palabra) > 10:
        print(f'Hay una palabra con mas de 10 caracteres: {palabra}')
        break
else:
    print('No hay palabras de mas de 10 caracteres')