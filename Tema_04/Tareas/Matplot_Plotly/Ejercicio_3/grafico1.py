# 3. Análisis de Datos de Redes Sociales
# Actividad de publicaciones a lo largo del tiempo: Gráficos de líneas para mostrar la frecuencia de publicaciones en 
# una plataforma de redes sociales a lo largo del tiempo, pudiendo destacar eventos específicos que causaron picos de actividad.
# Distribución de temas de conversación: Gráficos de barras o nubes de palabras para visualizar los temas más discutidos en las 
# redes sociales durante un período específico.
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
dias = np.arange(1, 31)

# Actividad de publicaciones por plataforma
plataformas = {
    'Twitter': np.random.randint(200, 500, 30),
    'Instagram': np.random.randint(150, 400, 30),
    'Facebook': np.random.randint(100, 300, 30)
}

# Gráfico
figura, ax = plt.subplots(figsize=(12, 5))

for plataforma, actividad in plataformas.items():
    ax.plot(dias, actividad, label=plataforma)

# Personalizacion
ax.set_title('Actividad de Publicaciones')
ax.set_xlabel('Día')
ax.set_ylabel('Nº de Publicaciones')
ax.legend()
plt.show()