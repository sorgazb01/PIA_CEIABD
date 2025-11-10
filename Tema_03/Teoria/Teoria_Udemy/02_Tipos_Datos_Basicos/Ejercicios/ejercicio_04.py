# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.

horaSalida = int(input("Introduce la hora de salida: "))
minutoSalida = int(input("Introduce los minutos de salida:"))
segundoSalida = int(input("Introduce los segundos de salida: "))
tiempoViaje = int(input("Introduce el tiempo del viaje en segundos: "))

tiempoSalida = (horaSalida * 3600) + (minutoSalida * 60) + segundoSalida

tiempoFinal = tiempoSalida + tiempoViaje

horaLlegada = tiempoFinal //3600
minutoLlegada = (tiempoFinal % 3600) // 60
segundoLlegada = (tiempoFinal % 3600) % 60

print("Hora de llegada: ", horaLlegada, ':', minutoLlegada, ':', segundoLlegada)