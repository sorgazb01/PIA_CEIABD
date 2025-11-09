# Un alumno desea saber cual será su calificación final en la materia
# Dicha calificación se compone de los siguientes porcentajes:
# * 55% del promedio de sus tres calificaciones parciales.
# * 30% de la calificación del examen final.
# * 15% de la calificación de un trabajo final.

parcial1 = float(input("Introduce la nota del parcial 1: "))
parcial2 = float(input("Introduce la nota del parcial 2: "))
parcial3 = float(input("Introduce la nota del parcial 3: "))
examenFinal = float(input("Introduce la nota del examen final: "))
trabajoFinal = float(input("Introduce la nota del trabajo final: "))

mediaParciales = (parcial1 + parcial2 + parcial3) / 3

notaFinal = (mediaParciales * 0.55) + (examenFinal * 0.3) + (trabajoFinal * 0.15)

print(f"La nota final del alumno es: {round(notaFinal, 2)}")