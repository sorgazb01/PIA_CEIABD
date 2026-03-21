# 5. Análisis de Tráfico Web
# Visitas y fuentes de tráfico web: Gráficos de líneas para mostrar la evolución de las visitas a un sitio web y 
# gráficos de barras apiladas o gráficos circulares para desglosar esas visitas por fuente de tráfico
# (directo, redes sociales, búsqueda, etc.). Tasa de rebote y tiempo de permanencia: Gráficos de dispersión para analizar 
# la relación entre la tasa de rebote y el tiempo medio de permanencia en el sitio, posiblemente para diferentes 
# categorías de páginas.
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# Datos por categoría de página
categorias = {
    'Blog': (np.random.randint(120, 300, 20), np.random.randint(20, 50, 20)),
    'Producto': (np.random.randint(60, 180, 20),  np.random.randint(40, 70, 20)),
    'Inicio': (np.random.randint(30, 90, 20),   np.random.randint(60, 85, 20)),
    'Contacto': (np.random.randint(20, 60, 20),   np.random.randint(70, 95, 20))
}

figura, ax = plt.subplots(figsize=(10, 6))

for categoria, (tiempo, rebote) in categorias.items():
    ax.scatter(tiempo, rebote, label=categoria, alpha=0.7)

# Personalizacion
ax.set_title('Tasa de Rebote vs Tiempo de Permanencia')
ax.set_xlabel('Tiempo de permanencia (seg)')
ax.set_ylabel('Tasa de rebote (%)')
ax.legend()
plt.show()