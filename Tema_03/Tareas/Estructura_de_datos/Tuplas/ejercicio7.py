### Ejercicio 7
# Modifica el ejercicio 6 para crear una lista de tuplas donde, aparezcan el divisor,el dividendo, la operación (%) y el resultado.
# Ejemplo:
# **lista_resultado = [(10, 5, '%', 0), (4, 6, '%', 4), (5, 7, '%', 5), (6, 5, '%', 1)]**
#### Solución:


tupla1 = (10, 4, 5, 6)
tupla2 = (5, 6, 7, 5)

lista_resultado = []

tupla_zip = zip(tupla1, tupla2)
for elemento in tupla_zip:
    divisor = elemento[0]
    dividendo = elemento[1]
    operando = '%'
    resultado = divisor % dividendo
    tupla_resultado = (divisor, dividendo, operando, resultado)
    lista_resultado.append(tupla_resultado)

print(lista_resultado)