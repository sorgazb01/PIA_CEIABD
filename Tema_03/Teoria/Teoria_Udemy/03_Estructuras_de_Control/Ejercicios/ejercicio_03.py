# Algoritmo que pida tres números y los muestre ordenados de mayor a menor.
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    if numero2 >= numero3:
        print(f"Números ordenados de mayor a menor: {numero1}, {numero2}, {numero3}")
    else:
        print(f"Números ordenados de mayor a menor: {numero1}, {numero3}, {numero2}")
elif numero2 >= numero1 and numero2 >= numero3:
    if numero1 >= numero3:
        print(f"Números ordenados de mayor a menor: {numero2}, {numero1}, {numero3}")
    else:
        print(f"Números ordenados de mayor a menor: {numero2}, {numero3}, {numero1}")
elif numero3 >= numero1 and numero3 >= numero2:
    if numero1 >= numero2:
        print(f"Números ordenados de mayor a menor: {numero3}, {numero1}, {numero2}")
    else:
        print(f"Números ordenados de mayor a menor: {numero3}, {numero2}, {numero1}")