# Ejercicio 9
# Dada la siguiente estructura de datos:
# alumnos = [{"Pedro":[5,7,9]},{"Sergio":[3,3,3]},{"Ibtihal":[5,5,5]},{"Angel":[7,7,9]},{"Fede":[5,5,7]}, {"Mik": [7,5,10]}]
# Devuelve el nombre y la nota media con 1 decimal de los alumnos cuya nombre tiene 4 letras o más y su nota media es superior a 6.
# a) Implementa el algoritmo utilizando bucles de la manera habitual.
# b) Soluciona el problema utilizando comprension de listas

alumnos = [{"Pedro":[5,7,9]},{"Sergio":[3,3,3]},{"Ibtihal":[5,5,5]},{"Angel":[7,7,9]},{"Fede":[5,5,7]}, {"Mik": [7,5,10]}]

# a) Sin comprensiones

# Metodo para obtener los alumnos que cumplan determinada condicion
def alumnosCondiciones(alumnos):
    resultado = []
    for alumno in alumnos:
        for nombre, notas in alumno.items():
            notaMedia = sum(notas)/len(notas)
            if len(nombre) >= 4 and notaMedia > 6:
                alumno[nombre] = round(notaMedia, 1)
                resultado.append(alumno)
    return resultado

print('Alumnos que cumplen las condiciones sin comprension: ')
print(alumnosCondiciones(alumnos))


# b) Con comprensiones
