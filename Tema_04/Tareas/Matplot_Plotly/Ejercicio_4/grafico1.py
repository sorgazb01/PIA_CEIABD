# 4. Análisis de Consumo Energético
# Consumo energético a lo largo del tiempo: Gráficos de áreas para mostrar el consumo de diferentes tipos de energía 
# (solar, eólica, fósil) a lo largo del tiempo, destacando cambios en la mezcla energética. Comparación del consumo energético por 
# sector: Gráficos de barras para comparar el consumo energético entre diferentes sectores (industrial, residencial, transporte) 
# en un año específico.
import matplotlib.pyplot as plt
import numpy as np

meses = np.arange(1, 13)

# Consumo por tipo de energía (en TWh)
energia = {
    'Solar':  [10, 12, 18, 25, 35, 42, 45, 40, 30, 20, 13, 10],
    'Eólica': [30, 28, 25, 20, 18, 15, 14, 16, 22, 27, 31, 33],
    'Fósil':  [80, 78, 70, 60, 50, 42, 40, 44, 55, 65, 75, 82]
}

# Gráfico de áreas
figura, ax = plt.subplots(figsize=(12, 5))

ax.stackplot(meses, energia.values(), labels=energia.keys(), alpha=0.7)
ax.set_title('Consumo Energético por Tipo')
ax.set_xlabel('Mes')
ax.set_ylabel('Consumo (TWh)')
ax.legend()
plt.show()