def leerFecha():
    dia = int(input('Introduce Día:'))
    mes = int(input('Introduce Mes: '))
    anio = int(input('Introduce Año: '))
    return dia,mes,anio

def Calcular_Dia_Juliano(dia, mes, anio):
    dia_juliano = 0
    for mes in range(1, mes):
        dia_juliano = dia_juliano + DiasDelMes(mes, anio)
    dia_juliano = dia_juliano + dia
    return dia_juliano

def DiasDelMes(mes, anio):
    if mes in [1,3,5,7,8,10,12]:
        return 31
    if mes == 2:
        if EsAnioBisiesto(anio):
            return 29
        else:
            return 28
    else:
        return 30
    
def EsAnioBisiesto(anio):
    return (anio % 4 == 0 and not (anio % 100 == 0) or anio % 400 == 0)

dia, mes, anio = leerFecha()
print(f'El dia juliano es {Calcular_Dia_Juliano(dia,mes,anio)}')