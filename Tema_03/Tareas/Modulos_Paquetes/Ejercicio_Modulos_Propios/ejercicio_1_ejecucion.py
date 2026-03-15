import ejercicio_1_modulo as modulo

def main():
    lista = modulo.generarLista()
    print("Lista generada:")
    modulo.mostrarLista(lista)

    lista_ordenada = modulo.ordenarLista(lista)
    print("Lista ordenada:")
    modulo.mostrarLista(lista_ordenada)

main()