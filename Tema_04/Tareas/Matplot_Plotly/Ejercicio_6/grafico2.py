# 6. Análisis de Ventas y Marketing
# Evolución de las ventas a lo largo del tiempo: Gráficos de líneas para mostrar las tendencias de ventas mensuales 
# o anuales, con la posibilidad de desglosar por categorías de productos. Rendimiento de campañas de marketing: 
# Gráficos de barras para comparar el retorno de la inversión (ROI) de diferentes campañas de marketing, 
# incluyendo canales online y offline.
import matplotlib.pyplot as plt

campañas = ['SEO', 'Email', 'Redes Sociales', 'TV', 'Radio', 'Prensa']
roi = [320, 280, 210, 150, 120, 90]

figura, ax = plt.subplots(figsize=(10, 5))
ax.bar(campañas, roi)

# Personalizacion
ax.set_title('ROI por Campaña de Marketing')
ax.set_xlabel('Canal')
ax.set_ylabel('ROI (%)')
plt.show()