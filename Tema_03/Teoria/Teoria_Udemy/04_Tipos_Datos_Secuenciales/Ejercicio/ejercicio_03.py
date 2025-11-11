# Suponiendo que hemos introducido una cadena por teclado
# que representa una frase
# (palabras separadas por espacios), realiza un programa que cuente cuantas
# palabras tiene.

cont = 0
posicion = 0
cad = input("Introduce una cadena: ")

cad = cad.strip()

posicion = cad.find(" ", posicion)

while posicion != -1:
    cont = cont + 1
    while cad[posicion + 1] == ' ':
        posicion = posicion + 1
    posicion = cad.find(" ", posicion + 1)
print("La frase tiene ",cont + 1," palabras.")