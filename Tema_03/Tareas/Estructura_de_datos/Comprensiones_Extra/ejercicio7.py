# 7. Combinando filtros y condicionales.
# ¡Este ejercicio de comprensiones combinaremos filtros con expresiones condicionales!
# Tienes algunos datos sobre porcentajes que necesitamos formatear de la misma manera. 
# Ignoraremos aquellos valores a None.
# El formato que queremos conseguir para todos los valores de la lista es:
# Float con dos decimales seguido del %
# Buena suerte 🚀
# Solución:

# Ejemplo de datos
porcentajes = [12,"23.5", None, 98.125, None, "73", 25.1, "55.238", 87, None, 21.02]

# Metodo para establecer los porcentajes normalizados
def obtenerPorcentajes(porcentajes):
    # Filtramos los valores en el formato adecuado, recorremos la lista y no tenemos
    # en cuenta los valores None
    return [f"{float(valor):.2f}%" for valor in porcentajes if valor is not None]

print(obtenerPorcentajes(porcentajes))
