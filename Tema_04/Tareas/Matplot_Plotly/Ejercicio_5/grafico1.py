# 5. Análisis de Tráfico Web
# Visitas y fuentes de tráfico web: Gráficos de líneas para mostrar la evolución de las visitas a un sitio web y 
# gráficos de barras apiladas o gráficos circulares para desglosar esas visitas por fuente de tráfico
# (directo, redes sociales, búsqueda, etc.). Tasa de rebote y tiempo de permanencia: Gráficos de dispersión para analizar 
# la relación entre la tasa de rebote y el tiempo medio de permanencia en el sitio, posiblemente para diferentes 
# categorías de páginas.
import matplotlib.pyplot as plt
import numpy as np

semanas = np.arange(1, 27)

# Visitas por fuente
fuentes = {
    'Búsqueda': np.random.randint(800, 1500, 26),
    'Redes Sociales': np.random.randint(400, 900, 26),
    'Directo': np.random.randint(300, 700, 26)
}

figura, ax = plt.subplots(figsize=(12, 5))

for fuente, visitas in fuentes.items():
    ax.plot(semanas, visitas, label=fuente)

# Personalizacion
ax.set_title('Evolución de Visitas por Fuente')
ax.set_xlabel('Semana')
ax.set_ylabel('Nº de Visitas')
ax.legend()
plt.show()