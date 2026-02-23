# 7 - Expresiones Equilibradas
# Crea un función que compruebe si los paréntesis, llaves y corchetes de una 
# expresión están equilibrados.
# Equilibrado significa que estos delimitadores se abren y cieran en orden y de 
# forma correcta.
# Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante 
# que otro.
# Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# Expresión no balanceada: { a * ( c + d ) ] - 5 }

# Función para comprobar si una expresión está equilibrada
def expresionEquilibrada(expresion):
    pila = []
    apertura = {"(", "[", "{"}
    cierre = {")": "(", "]": "[", "}": "{"}
    # Recorrer cada caracter de la expresión
    for caracter in expresion:
        # Si el caracter es un delimitador de apertura, lo agregamos a la pila
        if caracter in apertura:
            pila.append(caracter)
        # Si el caracter es un delimitador de cierre, verificamos si coincide 
        # con el último delimitador de apertura en la pila
        elif caracter in cierre:
            # Si la pila está vacía o el último delimitador de apertura no 
            # coincide con el delimitador de cierre, la expresión no está equilibrada
            if len(pila) == 0 or pila[-1] != cierre[caracter]:
                return False
            pila.pop()

    return len(pila) == 0

print(expresionEquilibrada("{ [ a * ( c + d ) ] - 5 }"))
print(expresionEquilibrada("{ a * ( c + d ) ] - 5 }"))
print(expresionEquilibrada("( [ ) ]"))
print(expresionEquilibrada("((()))"))
