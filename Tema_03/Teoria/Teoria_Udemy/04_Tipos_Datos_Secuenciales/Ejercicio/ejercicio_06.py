#Se quiere realizar un programa que lea por teclado las 5 notas 
# obtenidas por un alumno (comprendidas entre 0 y 10). A continuación
# debe mostrar todas las notas, la nota media, la nota más alta que 
# ha sacado y la menor.

notas = []

for indice in range(1,6):
    while True:
        nota = int(input(f'Introduce la nota {indice} :'))
        if nota >= 0 and nota <= 10: break
    notas.append(nota)
   
print("Notas: ")
for nota in notas:
    print(nota)
print(f'Nota media: {sum(notas)/len(notas)}')
print(f'Nota mmás alta: {max(notas)}')
print(f'Nota más baja: {min(notas)}') 