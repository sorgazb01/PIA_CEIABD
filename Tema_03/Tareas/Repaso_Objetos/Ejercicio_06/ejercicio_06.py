# 6. Crea una clase Empleado con atributos nombre, puesto y salario. Luego, crea
# una subclase Gerente que añada un atributo departamento y un método
# informar.
from empleado import Empleado
from gerente import Gerente

empleado = Empleado('Juan', 'Vigilante', 2200)
gerente = Gerente('Maria', 'Jefa Departamento', 3600, 'RRHH')
print(gerente.informar())