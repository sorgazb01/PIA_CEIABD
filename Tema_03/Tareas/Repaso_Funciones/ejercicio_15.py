# 15. Crear un programa que imprima una pirámide de asteriscos.
# Escribe una función que imprima una pirámide de N niveles usando 
# bucles.
import os

def piramide(niveles):
    for i in range(niveles * 2):
        asteriscos = ''
        espacio1 = ' '
        espacio2 = ' '
        for j in range(i + 1):
            asteriscos = asteriscos + '*'
        if j % 2 == 0:
            print((espacio1 + asteriscos + espacio2).center(os.get_terminal_size().columns))
        
piramide(15)