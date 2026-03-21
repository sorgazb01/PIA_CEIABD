# 2. Análisis de Datos de Salud
# Tasa de incidencia de enfermedades: Gráficos de barras para comparar la tasa de incidencia de una enfermedad específica a lo 
# largo de diferentes regiones o países. Evolución de la pandemia: Gráficos de líneas o áreas para mostrar la evolución diaria o 
# semanal de casos y muertes debido a una pandemia, con la posibilidad de incluir varias líneas para diferentes regiones o países.
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
semanas = np.arange(1, 27)

# Datos de casos por región
regiones = {
    'España': [8000 * np.exp(-((semana - 12)**2) / 18) for semana in semanas],
    'Francia': [11000 * np.exp(-((semana - 10)**2) / 18) for semana in semanas],
    'Italia': [9500 * np.exp(-((semana - 11)**2) / 18) for semana in semanas],
    'Alemania': [12000 * np.exp(-((semana - 13)**2) / 18) for semana in semanas]
}

# Gráfico de líneas – Casos
figura, ejes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

for region, casos in regiones.items():
    ejes[0].plot(semanas, casos, label=region)
    ejes[1].plot(semanas, np.array(casos) * 0.015, label=region)

# Personalización
ejes[0].set_title('Evolución Semanal de Casos – Pandemia 2024')
ejes[0].set_ylabel('Nº de Casos')
ejes[0].legend()

ejes[1].set_title('Evolución Semanal de Muertes – Pandemia 2024')
ejes[1].set_xlabel('Semana')
ejes[1].set_ylabel('Nº de Muertes')
ejes[1].legend()

plt.tight_layout()
plt.show()