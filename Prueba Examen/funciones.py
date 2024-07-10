import random as rd 
from statistics import geometric_mean
import csv

def asignar_sueldos(trabajadores):
    lista_trabajadores = []
    solo_sueldos_liquidos = {}

    for trabajador in trabajadores:
        sueldo_base = rd.randint(300000,2500000)
        desc_salud = round(sueldo_base * 0.07)
        desc_AFP = round(sueldo_base * 0.12)
        sueldo_liquido = sueldo_base - desc_AFP - desc_salud
        solo_sueldos_liquidos[trabajador] = sueldo_liquido

        info_trabajdor = {
            "nombre" : trabajador,
            "sueldo base" : sueldo_base,
            "desc salud" : desc_salud,
            "desc AFP" : desc_AFP,
            "sueldo liquido" : sueldo_liquido
        }
        lista_trabajadores.append(info_trabajdor)

    print("Sueldos generados con exito!!!")
    return lista_trabajadores,solo_sueldos_liquidos


def clasificar_sueldos(solo_sueldos_liquidos):

    menor_800 = {}
    entre_800_2k = {}
    mayor_2k = {}
    total = list(solo_sueldos_liquidos.values())
    TOTAL = sum(total)
    for trabajador,sueldos in solo_sueldos_liquidos.items():
        if sueldos < 800000:
            menor_800[trabajador] = sueldos
        elif sueldos <= 2000000:
            entre_800_2k[trabajador] = sueldos
        else:
            mayor_2k[trabajador] = sueldos
    
    print("-------------------------------------")
    print("Sueldos menores a $800k TOTAL:",len(menor_800))
    for trabajador,sueldos in menor_800.items():
        print(f"{trabajador} ${sueldos}")
    print("-------------------------------------")
    print("Sueldos entre $800k y $2000k TOTAL:",len(entre_800_2k))
    for trabajador,sueldos in entre_800_2k.items():
        print(f"{trabajador} ${sueldos}")
    print("-------------------------------------")
    print("Sueldos superiores a $2000k TOTAL:",len(mayor_2k))
    for trabajador,sueldos in mayor_2k.items():
        print(f"{trabajador} ${sueldos}")
    print("-------------------------------------")
    print(f"TOTAL SUELDOS: ${TOTAL}")


def ver_estadisticas(solo_sueldos_liquidos):
    sueldos = list(solo_sueldos_liquidos.values())

    sueldo_alto = max(sueldos)
    sueldo_bajo = min(sueldos)
    prom_sueldos = round(sum(sueldos) / len(sueldos))
    media_geo =round(geometric_mean(sueldos))

    return sueldo_alto,sueldo_bajo,prom_sueldos,media_geo


def reporte_sueldos(lista_trabajadores):
    print("Empleados\t|Sueldo Base\t   |Desc. Salud\t|Desc. AFP\t|Sueldo Liquido")
    print("---------------------------------------------------------------------------------------")
    for trabajador in lista_trabajadores:
        print(f"{trabajador["nombre"]}\t|{trabajador["sueldo base"]}\t    |{trabajador["desc salud"]}\t  |{trabajador["desc AFP"]}\t  |{trabajador["sueldo liquido"]}")


def exportar_archivo(lista_trabajadores):
    with open("informe_trabajadores.csv","w",newline="") as archivo:

        escritor = csv.writer(archivo,delimiter=",")

        escritor.writerow(["Nombre Empleado","Sueldo Base","Desc. Salud","Desc. AFP","Sueldo Liquido"])
        
        for trabajador in lista_trabajadores:
            nombre = trabajador["nombre"]
            sueldo_base = trabajador["sueldo base"]
            desc_salud = trabajador["desc salud"]
            desc_AFP = trabajador["desc AFP"]
            sueldo_liquido = trabajador["sueldo liquido"]
            escritor.writerow([nombre,sueldo_base,desc_salud,desc_AFP,sueldo_liquido])
    print("Informe generado con exito!!")


