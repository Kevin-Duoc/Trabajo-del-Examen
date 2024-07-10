import funciones as fn 

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Roco","Laura Hernan","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Reyes"]
lista_trabajadores ={}
solo_sueldos_liquidos = {}

opcion = None
while opcion != 6:
    print("""        ~~~~~~~~~~~~~~~~~
        MENU TRABAJADORES
        ~~~~~~~~~~~~~~~~~
1.- Asignar sueldos aleatorios
2.- Clasificar sueldos
3.- Ver estadisticas
4.- Reporte de sueldos
5.- Exportar archivo
6.- Salir del programa""")
    try:
        opcion = int(input("--> "))
        if opcion == 1:
            lista_trabajadores,solo_sueldos_liquidos = fn.asignar_sueldos(trabajadores)
        
        elif opcion == 2:
            if lista_trabajadores:
                fn.clasificar_sueldos(solo_sueldos_liquidos)
            else:
                print("Primero debe de asignar los sueldos")
        
        elif opcion == 3:
            if lista_trabajadores:
                sueldo_alto,sueldo_bajo,prom_sueldos,media_geo = fn.ver_estadisticas(solo_sueldos_liquidos)
                print("-----------------------------")
                print(f"Sueldo mas alto: ${sueldo_alto}")
                print(f"Sueldo mas bajo: ${sueldo_bajo}")
                print(f"Promedio de sueldos: ${prom_sueldos}")
                print(f"Media geometrica: ${media_geo}")
                print("-----------------------------")
            else:
                print("Primero debe de asignar los sueldos")

        elif opcion == 4:
            if lista_trabajadores:
                fn.reporte_sueldos(lista_trabajadores)
            else:
                print("Primero debe de asignar los sueldos")
        
        elif opcion == 5:
            if lista_trabajadores:
                fn.exportar_archivo(lista_trabajadores)
            else:
                print("Primero debe de asignar los sueldos")
        elif opcion == 6:
            print("Finalizando programa...")
            print("Desarrollado por Kevin Fuenzalida")
            print("RUT 20.657.966-8")
    except ValueError:
        print()

