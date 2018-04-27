import time


# Seccion de Menus y partes Graficas de bajo nivel

def menu_principal():
    print ("\n|-----------------------------------|")
    print ("|                MENU               |")
    print ("|-----------------------------------|")
    print ("|1. Programa en python 1            |")
    print ("|2. Codigo en c                     |")
    print ("|3. Ejecutar programa c             |")
    print ("|4. Programa en python Laboratorio  |")
    print ("|5. Codigo en c                     |")
    print ("|6. Ejecutar programa c             |")
    print ("|7. Salir                           |")
    print ("|-----------------------------------|")


def pantalla_carga():
    print ("|-------------------------------------------------------------|")
    print ("|                                                             |")
    print ("|                          CARGANDO..                         |")
    print ("|                                                             |")
    print ("|-------------------------------------------------------------|\n")
    for i in range(0, 32):
        print'*',
        time.sleep(.025)


def bienvenido():
    print("------------------------------------------------------------------------------")
    print"  ____    _ "
    print" | __ )  (_)   ___   _ __   __   __   ___   _ __   (_)   __| |   ___    ___ "
    print" |  _ \  | |  / _ \ | '_ \  \ \ / /  / _ \ | '_ \  | |  / _` |  / _ \  / __|"
    print" | |_) | | | |  __/ | | | |  \ V /  |  __/ | | | | | | | (_| | | (_) | \__ \ "
    print" |____/  |_|  \___| |_| |_|   \_/    \___| |_| |_| |_|  \__,_|  \___/  |___/"
    print("------------------------------------------------------------------------------")


def resultado():

    print(" __                             ")
    print("|__)  _  _     | |_  _   _|  _  ")
    print("| \  (- _) |_| | |_ (_| (_| (_) ")


# Fin de la seccion  de Menus y partes Graficas de bajo nivel, inicio de funciones y procedimientos

def calcular_dias_que_tarda(altura,subida,bajada):
    while (altura < 0 or subida < 0 or bajada < 0):
        print("Tu datos no fueron logicos la altura no puede ser mas alta que lo que sube y lo que sube no puede ser mas de lo que baja")
        altura = input("Dame la altura en metros del arbol: ")
        subida = input("Dame los metros que sube por dia: ")
        bajada = input("Dame los metros que baja por noche: ")
    dias_que_tarda = 0
    aux = altura - subida
    while aux > 0:
        altura = (altura - subida) + bajada
        dias_que_tarda = dias_que_tarda + 1
        aux = altura - subida

    return dias_que_tarda +1
