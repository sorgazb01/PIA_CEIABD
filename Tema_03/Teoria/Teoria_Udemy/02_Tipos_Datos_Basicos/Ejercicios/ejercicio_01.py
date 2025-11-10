# Dados los catetos de un triángulo rectángulo,
# calcular su hipotenusa.

import math

cateto1 = float(input("Introduce la medida del primer cateto: "))
cateto2 = float(input("Introduce la medida del segundo cateto: "))

hipotenusa = math.sqrt(pow(cateto1, 2) + pow(cateto2, 2))

print(f"La hipotusa del triángulo rectángulo es: {round(hipotenusa, 2)}")