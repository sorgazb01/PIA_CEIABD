# 8. Modifica la clase Animal para que cada subclase (Perro, Gato) tenga un
# método hacer_sonido que imprima un sonido diferente según el tipo de
# animal. Llama al método en un objeto de cada clase.
from perro import Perro
from gato import Gato

perro = Perro("Perro")
gato = Gato("Gato")

perro.hacer_sonido()
gato.hacer_sonido()