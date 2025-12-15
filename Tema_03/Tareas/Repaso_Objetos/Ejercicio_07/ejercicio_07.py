# 7. Crea una clase Vehículo con un atributo marca. Luego, crea las subclases
# Coche y Camión, cada una con un atributo adicional (por ejemplo, puertas y
# capacidad respectivamente).
from vehiculo import Vehiculo
from coche import Coche
from camion import Camion

vehiculo = Vehiculo('Renault')
coche = Coche('BMW', 5)
camion = Camion('Iveco', 30000)