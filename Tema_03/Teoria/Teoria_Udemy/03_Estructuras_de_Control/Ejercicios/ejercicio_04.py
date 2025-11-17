# Escribe un programa que pida una fecha (día, mes y año) y diga si el mes tiene 31, 30 o 28 dias.

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año:"))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_mes = 30
elif mes == 2:
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dias_mes = 29
    else:
        dias_mes = 28
else:
    print("Fecha no válida.")
    
if dia < 0 or dia > dias_mes:
    print("Fecha no válida.")
else:
    print(f"El mes {mes} del año {anio} tiene {dias_mes} días.")