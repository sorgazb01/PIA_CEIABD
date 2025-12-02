# 5. Generar la tabla de multiplicar de un número.
# Escribe una función que genere la tabla de multiplicar de un número 
# (por ejemplo, tabla del 3).

def tablaMultiplicar(numero):
    for x in range(0, 11):
        print(f"{numero} x {x} = {numero * x}")
        
numero = int(input("Introduce un numero para obtener su tabla de multiplicar: "))
tablaMultiplicar(numero)