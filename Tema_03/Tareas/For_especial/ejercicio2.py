# Ejercicio 2
# Dado un conjunto de nombres, determina si hay algún nombre que empiece con la letra "A". 
# Si hay al menos un nombre que empiece con la letra "A", imprime el primer nombre 
# encontrado que cumpla con este criterio. Si no hay ningún nombre que empiece con la 
# letra "A", imprime un mensaje indicando que no se encontró ningún nombre que cumpla 
# con este criterio.

nombres = ['Juan', 'Ana', 'Pedro', 'Luis', 'Sergio']

for nombre in nombres:
    if nombre[0].lower() == 'a':
        print(f'Hay un nombre que empieza por la A: {nombre}')
        break
else:
    print('No hay nombres que empiecen por la A')