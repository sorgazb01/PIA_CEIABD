nota = int(input("Introduce una nota: "))
if (nota < 5):
    print("Suspenso")
elif (nota == 5):
    print("Suficiente")
elif (nota == 6):
    print("Bien")
elif (nota >= 7 and nota <= 8):
    print("Notable")
elif (nota >= 9 and nota <= 10):
    print("Sobresaliente")
else:
    print("La nota introducida no es correcta.")
print("Programa terminado.")