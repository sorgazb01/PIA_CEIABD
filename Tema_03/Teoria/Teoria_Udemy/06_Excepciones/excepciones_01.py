# while True print('Hello world')
# 4 / 0
# a + 4
# "2" + 2
#  num = int(input("Numero: ")) -> valor de cadena

while True:
    try:
        x = int(input("Introduce un número: "))
        break
    except ValueError:
        print('Error, debes introducir un número.')
        
cad = input('Dime un número: ')
try:
    print(10/int(cad))
except ValueError:
    print('No se puede convertir a entero.')
except ZeroDivisionError:
    print('No se puede dividir entre 0.')
else:
    print('Se ha producido un error')
finally:
    print('Se ejecuta siempre al final.')