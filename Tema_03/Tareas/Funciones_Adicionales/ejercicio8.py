# 8-  Carrera de Obstaculos
# Crea una función que evalúe si un/a atleta ha superado correctamente una carrera 
# de obstáculos.
# La función recibirá dos parámetros:
# Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# Una lista que sólo puede contener String con las palabras "run" o "jump"
# La función imprimirá cómo ha finalizado la carrera:
# Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será 
# correcto y no variará el símbolo de esa parte de la pista.
# Si hace "jump" en "_" (suelo), se variará esa parte de la pista por "x".
# Si hace "run" en "|" (valla), se variará esa parte de la pista por "/".
# La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista.

# Funcion para comprobar si el atleta ha superado la carrera de obstaculos
def carreraObstaculos(pista, accion):
    # Convertimos la pista en una lista para poder modificarla
    resultado = list(pista)
    superada = True
    # Bucle para comprobar cada tramo de la pista con la accion correspondiente
    for i, (pista, action) in enumerate(zip(resultado, accion)):
        if pista == '_' and action == 'jump':
            resultado[i] = 'x'
            superada = False
        elif pista == '|' and action == 'run':
            resultado[i] = '/'
            superada = False
    print(''.join(resultado))
    return superada

print(carreraObstaculos("_|_|_", ["run", "jump", "run", "jump", "run"]))
print(carreraObstaculos("_|_|_", ["run", "run",  "run", "jump", "run"]))