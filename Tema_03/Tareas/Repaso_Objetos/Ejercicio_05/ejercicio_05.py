# 5. Crea una clase base Animal con el atributo nombre y un método descripción
# que imprima una descripción del animal. Crea una subclase Gato que herede
# de Animal y añada un método maullar.
from animal import Animal
from gato import Gato

animal = Animal('Animal')
gato = Gato('Gato')

print(f'{gato.maullar()}')