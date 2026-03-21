# 3. Análisis de Datos de Redes Sociales
# Actividad de publicaciones a lo largo del tiempo: Gráficos de líneas para mostrar la frecuencia de publicaciones en 
# una plataforma de redes sociales a lo largo del tiempo, pudiendo destacar eventos específicos que causaron picos de actividad.
# Distribución de temas de conversación: Gráficos de barras o nubes de palabras para visualizar los temas más discutidos en las 
# redes sociales durante un período específico.
import matplotlib.pyplot as plt

# Temas de conversación
temas = ['Política', 'Deporte', 'Tecnología', 'Música', 'Cine', 'Clima', 'Economía']
menciones = [4300, 3800, 3200, 2900, 2400, 2100, 1800]

# Gráfico
figura, ax = plt.subplots(figsize=(10, 5))
ax.bar(temas, menciones)

# Personalizacion
ax.set_title('Temas más Discutidos')
ax.set_xlabel('Tema')
ax.set_ylabel('Nº de Menciones')
plt.show()