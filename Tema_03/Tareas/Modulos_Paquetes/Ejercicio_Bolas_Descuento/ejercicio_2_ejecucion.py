from paquete import ejercicio_2_modulo as modulo

def main():
    totalCompra = float(input("Introduce el total de tu compra: "))

    if totalCompra < 100:
        print("Lo sentimos, no se aplica ninguna promoción para compras inferiores a 100.00€.")
    else:
        bola = modulo.seleccionarBola()
        porcentaje = modulo.obtenerDescuento(bola)
        nuevoTotal = modulo.calcularTotal(totalCompra, porcentaje)
        modulo.mostrarResultado(totalCompra, bola, porcentaje, nuevoTotal)

main()