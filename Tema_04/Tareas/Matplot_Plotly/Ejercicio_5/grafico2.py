# 5. Análisis de Tráfico Web
# Visitas y fuentes de tráfico web: Gráficos de líneas para mostrar la evolución de las visitas a un sitio web y 
# gráficos de barras apiladas o gráficos circulares para desglosar esas visitas por fuente de tráfico
# (directo, redes sociales, búsqueda, etc.). Tasa de rebote y tiempo de permanencia: Gráficos de dispersión para analizar 
# la relación entre la tasa de rebote y el tiempo medio de permanencia en el sitio, posiblemente para diferentes 
# categorías de páginas.
import matplotlib.pyplot as plt

fuentes = ['Búsqueda', 'Redes Sociales', 'Directo', 'Referidos', 'Email']
porcentajes = [42, 25, 18, 10, 5]

figura, ax = plt.subplots(figsize=(7, 7))

ax.pie(porcentajes, labels=fuentes, autopct='%1.1f%%')
ax.set_title('Fuentes de Tráfico Web')
plt.show()