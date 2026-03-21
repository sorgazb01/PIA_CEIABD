# 6. Análisis de Ventas y Marketing
# Evolución de las ventas a lo largo del tiempo: Gráficos de líneas para mostrar las tendencias de ventas mensuales 
# o anuales, con la posibilidad de desglosar por categorías de productos. Rendimiento de campañas de marketing: 
# Gráficos de barras para comparar el retorno de la inversión (ROI) de diferentes campañas de marketing, 
# incluyendo canales online y offline.
import matplotlib.pyplot as plt
import numpy as np

meses = np.arange(1, 13)

# Ventas por categoría (en miles de €)
categorias = {
    'Electrónica': [85, 90, 95, 100, 110, 120, 130, 125, 115, 105, 140, 160],
    'Ropa': [60, 55, 65, 80, 75, 70, 85, 90, 95, 100, 120, 150],
    'Hogar': [40, 42, 45, 50, 55, 53, 48, 46, 52, 58, 70, 90]
}

figura, ax = plt.subplots(figsize=(12, 5))

for categoria, ventas in categorias.items():
    ax.plot(meses, ventas, marker='o', label=categoria)

# Personalizacion
ax.set_title('Evolución Mensual de Ventas por Categoría')
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas (miles €)')
ax.legend()
plt.show()
