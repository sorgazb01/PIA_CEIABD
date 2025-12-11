from empleado import Empleado

class Gerente(Empleado):
    
    def __init__(self, nombre, puesto, salario, departamento):
        super().__init__(nombre, salario, puesto)
        self.departamento = departamento
        
    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento
        
    def informar(self):
        return f"Gerente: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}, Departamento: {self.departamento}"