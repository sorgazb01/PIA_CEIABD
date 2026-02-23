# 9 - Piedra, Papel, Tijera
# Crea una función que calcule quien gana más partidas al piedra, papel, tijera.
# El resultado puede ser: "Jugador 1", "Jugador 2", "Empate" 
# La función recibe un listado que contiene tuplas, representando cada jugada.
# El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
# Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Jugador 2".

# Metodo para jugar al piedra, papel y tijera
def jugarPiedraPapelTijera(jugadas):
    # Contador de victorias de cada jugador
    victoriasJugador1 = 0
    victoriasJugador2 = 0
    # Bucle que recorre el diccionario con las jugadas y compara los resultados para aumnetar
    # los contadores de victorias de cada jugador
    for jugadaJugador1, jugadaJugador2 in jugadas:
        if jugadaJugador1 == jugadaJugador2:
            pass
        elif (jugadaJugador1 == "R" and jugadaJugador2 == "S") or (jugadaJugador1 == "S" and jugadaJugador2 == "P") or (jugadaJugador1 == "P" and jugadaJugador2 == "R"):
            victoriasJugador1 += 1
        else:
            victoriasJugador2 += 1
    # Resultados
    if victoriasJugador1 > victoriasJugador2:
        return "Jugador 1"
    elif victoriasJugador2 > victoriasJugador1:
        return "Jugador 2"
    else:
        return "Empate"

jugadas = [("R", "S"), ("S", "R"), ("P", "S")]
print(jugarPiedraPapelTijera(jugadas))