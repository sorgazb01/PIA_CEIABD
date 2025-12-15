# 9. Crea una clase Empleado con un método calcular_bonus que calcule el bono
# anual de un empleado. Luego, crea una subclase Vendedor que modifique el
# método para calcular el bono según las ventas realizadas.
from empleado import Empleado
from vendedor import Vendedor

empleado = Empleado('Pepe', 'Dependiente', 1300)
vendedor = Vendedor('Luis', 'Vendedor Jefe', 1300, 60)

print(f'El bonus del empleado {empleado.nombre} es de {empleado.calcular_bonus()}')
print(f'El bonus del vendedor {vendedor.nombre} es de {vendedor.calcular_bonus()}')