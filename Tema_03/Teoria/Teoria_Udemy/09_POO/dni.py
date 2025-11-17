class Dni():
    def __init__(self, numero):
        self.numero = numero
        
    def __calcular_letra(self):
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(self.numero)%23]
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def letra(self):
        return self._letra
    
    @numero.setter
    def numero(self, numero):
        if len(numero)==8 and numero.isdigit():
            self._numero = numero
            self._letra = self.__calcular_letra()
        else:
            self._numero = 0
            self._letra = ''
            print('DNI incorrecto')
            
    def mostrar(self):
        return self.numero+self.letra