import sqlite3

# Creamos la conexión
conexion = sqlite3.connect('estudiantes.db')

# creamos el cursor
c = conexion.cursor()  # cursor

#cremos la tabla estudiantes
c.execute("""CREATE TABLE estudiantes (
            nombre TEXT,
            edad INTEGER,
            altura REAL
    )""")

#fijaros que cada elemento de la lista es una tupla con los valores de cada campo de la tabla.
all_estudiantes = [
    ('Jon', 21, 1.8),
    ('David', 35, 1.7),
    ('Maite', 19, 1.83),
]
# al insertar, en VALUES usamos los ? para indicarle que queremos que coja los valores de la lista all_estudiantes.
c.executemany("INSERT INTO estudiantes VALUES (?, ?, ?)", all_estudiantes)

# Seleccionamos los datos y los mostramos
c.execute("SELECT * FROM estudiantes")
print(c.fetchall())

# confirmamos los cambios
conexion.commit()

# cerramos la conexión.
conexion.close()