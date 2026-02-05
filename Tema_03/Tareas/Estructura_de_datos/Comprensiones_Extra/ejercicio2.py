# 2. Tablero Ajedrez
# Las comprensiones de listas anidadas son excelentes cuando necesitas trabajar 
# con cuadrículas (2D) .
# ¿Puedes ayudarme a crear un tablero de ajedrez?
# Vamos a transformar el siguiente código a comprensiones 🚀 🚀 🚀
# Resultado:
# 
# [
# ['a8'], ['b8'], ['c8'], ['d8'], ['e8'], ['f8'], ['g8'],

# ['a7'], ['b7'], ['c7'], ['d7'], ['e7'], ['f7'], ['g7'],

# ['a6'], ['b6'], ['c6'], ['d6'], ['e6'], ['f6'], ['g6'],

# ['a5'], ['b5'], ['c5'], ['d5'], ['e5'], ['f5'], ['g5'],

# ['a4'], ['b4'], ['c4'], ['d4'], ['e4'], ['f4'], ['g4'],

# ['a3'], ['b3'], ['c3'], ['d3'], ['e3'], ['f3'], ['g3'],

# ['a2'], ['b2'], ['c2'], ['d2'], ['e2'], ['f2'], ['g2'],

# ['a1'], ['b1'], ['c1'], ['d1'], ['e1'], ['f1'], ['g1']
# ]
# Solución:

# Metodo para crear el tablero de ajedrez por compresiones
def crearTableroAjedrez():
    # Empezamos las filas por 8 y vamos restando 1 y las columnas en orden alfabetico
    tableroAjedrez = [[columna + str(fila)] for fila in range(8, 0, -1) for columna in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
    # Mostramos el tablero
    for columna in range(0, len(tableroAjedrez), 8):
        fila = tableroAjedrez[columna:columna+8]
        print(fila, end="")
        print()

crearTableroAjedrez()