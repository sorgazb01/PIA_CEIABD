# Ejercicio 2
# Normalización de datos de usuarios
# Una aplicación almacena información de usuarios en un diccionario donde las 
# claves son los IDs y los valores son tuplas con la edad y el ingreso mensual 
# de cada usuario. Escribe un programa que recorra el diccionario y cree una nueva 
# lista de tuplas, donde la edad e ingreso mensual estén normalizados entre 0 y 1 
# con respecto al máximo encontrado en cada categoría.
# 
# Nota sobre la normalización de datos:
# La normalización es un proceso matemático utilizado para escalar valores dentro 
# de un rango común, generalmente entre 0 y 1.
# Este proceso asegura que todos los valores estén representados proporcionalmente entre 0 y 1,
#  preservando las relaciones relativas entre ellos.

#Datos de Pruebas
usuarios = {
    1: (25, 3000),
    2: (None, 4500),  
    3: (22, None),    
    4: (30, 3800),
    5: (None, None),  
    6: (27, 5000),
}

# Metodo para obtener la edad maxima del diccionario
def calcularEdadMaxima(usuarios):
    edades = []
    for idUsuario, (edad, ingreso) in usuarios.items():
        if edad is not None:
            edades.append(edad)
    edadMaxima = max(edades)
    return edadMaxima

# Metodo para obtener los ingresos maximos del diccionario
def calcularIngresosMaximos(usuarios):
    ingresos = []
    for idUsuario, (edad, ingreso) in usuarios.items():
        if ingreso is not None:
            ingresos.append(ingreso)
    ingresosMaximos = max(ingresos)
    return ingresosMaximos

# Metodo para normalizar los valores de los usuarios
def normalizarUsuarios(usuarios):
    # Obtenemos la edad maxima
    edadMaxima = calcularEdadMaxima(usuarios)
    # Obtenemos los ingresos maximos
    ingresosMaximos = calcularIngresosMaximos(usuarios)

    # Listas de tuplas
    usuariosNormalizados = []
    # Recorremos los usuarios
    for idUsuario, (edad, ingreso) in usuarios.items():
        # Normalizamos los usuarios
        edadNormalizada = normalizar(edad, edadMaxima)
        ingresoNormalizado = normalizar(ingreso, ingresosMaximos)
        # Añadimos a la lista la tupla normalizada
        usuariosNormalizados.append((idUsuario, edadNormalizada, ingresoNormalizado))
    
    return usuariosNormalizados

# Metodo para normalizar valores
def normalizar (valor, maximo):
    valorNormalizado = 0
    if valor is None:
        valorNormalizado = None
    else:
        valorNormalizado = valor/maximo
    return valorNormalizado

print(normalizarUsuarios(usuarios))