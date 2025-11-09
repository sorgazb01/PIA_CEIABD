#!/usr/bin/env python3
"""
Snake - juego para terminal en Python (usa curses).

Controles:
 - Flechas o WASD para mover
 - Q para salir
 - R en la pantalla de "Game Over" para reiniciar

Requisitos:
 - Python 3
 - En Windows instala `windows-curses` (pip install windows-curses)

Guarda este archivo como `snake_game.py` y ejecútalo con:
    python snake_game.py

Disfruta y dime si quieres más características (niveles, paredes, guardar records...)
"""

import curses
import random
import time

MIN_WIDTH = 40
MIN_HEIGHT = 10


def place_food(snake, height, width):
    """Coloca la comida en una posición aleatoria que no choque con la serpiente."""
    while True:
        y = random.randint(1, height - 2)
        x = random.randint(1, width - 2)
        if [y, x] not in snake:
            return [y, x]


def draw_border(win):
    """Dibuja borde y cabecera con la puntuación (la ventana ya debe existir)."""
    win.border()


def game_loop(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(False)
    stdscr.clear()

    sh, sw = stdscr.getmaxyx()
    if sw < MIN_WIDTH or sh < MIN_HEIGHT:
        stdscr.addstr(0, 0, f"Terminal muy pequeña (mínimo {MIN_WIDTH}x{MIN_HEIGHT}). Amplía la ventana y prueba de nuevo.")
        stdscr.refresh()
        stdscr.getch()
        return

    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(True)
    win.nodelay(True)

    # Ajustes iniciales
    initial_speed = 150  # ms
    win.timeout(initial_speed)

    # Serpiente: lista de [y, x] (la cabeza es snake[0])
    start_x = sw // 4
    start_y = sh // 2
    snake = [[start_y, start_x], [start_y, start_x - 1], [start_y, start_x - 2]]

    direction = curses.KEY_RIGHT
    score = 0

    food = place_food(snake, sh, sw)

    paused = False

    while True:
        win.clear()
        draw_border(win)

        # Cabecera
        title = " SNAKE (Q salir, P pausar) "
        score_text = f"Puntos: {score}"
        try:
            win.addstr(0, 2, score_text)
            win.addstr(0, max(4, sw // 2 - len(title) // 2), title)
        except curses.error:
            # en casos raros de tamaño de terminal muy pequeño
            pass

        # Dibuja comida
        try:
            win.addch(food[0], food[1], "*")
        except curses.error:
            pass

        # Dibuja serpiente (cabeza distinta)
        for i, segment in enumerate(snake):
            ch = "@" if i == 0 else "#"
            try:
                win.addch(segment[0], segment[1], ch)
            except curses.error:
                pass

        # Input (no bloqueante)
        key = win.getch()

        if key in (ord('q'), ord('Q')):
            break
        if key in (ord('p'), ord('P')):
            paused = not paused
            if paused:
                try:
                    win.addstr(sh // 2, sw // 2 - 5, " PAUSADO ")
                except curses.error:
                    pass
                win.refresh()
            # loop to wait until unpaused
            while paused:
                k = win.getch()
                if k in (ord('p'), ord('P')):
                    paused = False
                elif k in (ord('q'), ord('Q')):
                    return
                time.sleep(0.05)
            # restaurar timeout cuando se reanuda
            win.timeout(initial_speed)

        # Mapear teclas WASD también
        if key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT):
            new_dir = key
        elif key in (ord('w'), ord('W')):
            new_dir = curses.KEY_UP
        elif key in (ord('s'), ord('S')):
            new_dir = curses.KEY_DOWN
        elif key in (ord('a'), ord('A')):
            new_dir = curses.KEY_LEFT
        elif key in (ord('d'), ord('D')):
            new_dir = curses.KEY_RIGHT
        elif key == -1:
            new_dir = direction
        else:
            new_dir = direction

        # Evitar giro de 180 grados
        opposites = {curses.KEY_UP: curses.KEY_DOWN, curses.KEY_DOWN: curses.KEY_UP,
                     curses.KEY_LEFT: curses.KEY_RIGHT, curses.KEY_RIGHT: curses.KEY_LEFT}
        if new_dir != opposites.get(direction, None):
            direction = new_dir

        # Calcula nueva cabeza según dirección
        head = snake[0].copy()
        if direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            head[1] += 1

        # Comprueba colisiones con paredes
        if head[0] == 0 or head[0] == sh - 1 or head[1] == 0 or head[1] == sw - 1:
            break

        # Comprueba colisión con el cuerpo
        if head in snake:
            break

        # Mover
        snake.insert(0, head)

        # Comer comida
        if head == food:
            score += 1
            # Aumenta velocidad ligeramente con la longitud
            new_speed = max(30, initial_speed - (len(snake) // 5) * 8)
            win.timeout(new_speed)
            food = place_food(snake, sh, sw)
        else:
            snake.pop()

        # pequeña espera para no saturar CPU; curses.timeout ya ayuda
        # pero dejamos esta micro-pausa
        time.sleep(0.01)

    # Pantalla final
    win.nodelay(False)
    msg = f"GAME OVER - Puntos: {score}"
    try:
        win.addstr(sh // 2 - 1, sw // 2 - len(msg) // 2, msg)
        win.addstr(sh // 2 + 1, sw // 2 - 14, "Pulsa R para reiniciar o Q para salir")
    except curses.error:
        pass
    win.refresh()

    while True:
        k = win.getch()
        if k in (ord('q'), ord('Q')):
            break
        if k in (ord('r'), ord('R')):
            # reinicia
            game_loop(stdscr)
            return


if __name__ == "__main__":
    try:
        curses.wrapper(game_loop)
    except KeyboardInterrupt:
        print("Juego terminado.")
