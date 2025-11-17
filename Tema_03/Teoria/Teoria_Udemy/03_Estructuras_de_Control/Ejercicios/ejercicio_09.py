# Escribe un programa que diga si un número introducido por teclado es primo.
# Un número primo es aquel que solo es divisible entre él mismo y 1

es_primo = True
numero_es_primo = int(input('Introduce un número para comprobar si es primo: '))
for num in range (2, numero_es_primo):
    if numero_es_primo % num == 0:
        es_primo = False
        break

if(es_primo == True):
    print(f'El numero {numero_es_primo} es primo')
else:
    print(f'El numero {numero_es_primo} no es primo')