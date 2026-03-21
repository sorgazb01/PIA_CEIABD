# 2. Análisis de Datos de Salud
# Tasa de incidencia de enfermedades: Gráficos de barras para comparar la tasa de incidencia de una enfermedad específica a lo 
# largo de diferentes regiones o países. Evolución de la pandemia: Gráficos de líneas o áreas para mostrar la evolución diaria o 
# semanal de casos y muertes debido a una pandemia, con la posibilidad de incluir varias líneas para diferentes regiones o países.
import matplotlib.pyplot as plt
import numpy as np

# Listado de paises y tasa de incidencia
paises = ['España', 'Francia', 'Alemania', 'Italia', 'Portugal', 'P. Bajos', 'Bélgica', 'Suecia']
incidencia = [142, 198, 175, 163, 121, 210, 187, 155]

# Grafico de barras
figura, ax = plt.subplots(figsize=(10, 6))
ax.bar(paises, incidencia)

# Personalizacion del grafico
ax.set_title('Incidencia de Gripe por País')
ax.set_xlabel('País')
ax.set_ylabel('Tasa de incidencia')
plt.show()