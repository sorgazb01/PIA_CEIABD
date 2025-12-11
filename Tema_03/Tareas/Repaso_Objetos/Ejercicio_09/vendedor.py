from empleado import Empleado
class Vendedor(Empleado):
    
    def __init__(self, nombre, puesto, salario, ventas):
        super().__init__(nombre, puesto, salario)
        self.ventas = ventas
        
    @property
    def ventas(self):
        return self._ventas
    
    @ventas.setter
    def ventas(self, ventas):
        self._ventas = ventas
        
    def calcular_bonus(self):
        return super().calcular_bonus() + (self.ventas * 0.02)
