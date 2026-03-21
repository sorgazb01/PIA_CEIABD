# 4. Análisis de Consumo Energético
# Consumo energético a lo largo del tiempo: Gráficos de áreas para mostrar el consumo de diferentes tipos de energía 
# (solar, eólica, fósil) a lo largo del tiempo, destacando cambios en la mezcla energética. Comparación del consumo energético por 
# sector: Gráficos de barras para comparar el consumo energético entre diferentes sectores (industrial, residencial, transporte) 
# en un año específico.
import matplotlib.pyplot as plt

sectores = ['Industrial', 'Residencial', 'Transporte', 'Comercial', 'Agricultura']
consumo = [520, 310, 280, 190, 95]

# Gráfico de barras
figura, ax = plt.subplots(figsize=(10, 5))
ax.bar(sectores, consumo)

# Personalizacion
ax.set_title('Consumo Energético por Sector')
ax.set_xlabel('Sector')
ax.set_ylabel('Consumo (TWh)')
plt.show()