import time


def menu_principal():
    print ("\n|----------------------------|")
    print ("|            MENU            |")
    print ("|----------------------------|")
    print ("|1. Programa en python-1     |")
    print ("|2. Mostrar Archivo de C P1  |")
    print ("|3. Salir                    |")
    print ("|----------------------------|")


def cargando():
    print ("|-------------------------------------------------------------|")
    print ("|                                                             |")
    print ("|                          CARGANDO..                         |")
    print ("|                                                             |")
    print ("|-------------------------------------------------------------|\n")
    for i in range(0, 32):
        print'*',
        j=j+1
        time.sleep(.025)

