class Estudiante:
    
    def __inti__(self, nombre, edad, nota_media):
        self.nombre = nombre
        self.edad = edad
        self.nota_media = nota_media
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def nota_media(self):
        return self._nota_media
    
    @nota_media.setter
    def nota_media(self, nota_media):
        self._nota_media = nota_media
        
    def aprobado(self):
        if self.nota_media >= 5:
            return True
        else:
            return False