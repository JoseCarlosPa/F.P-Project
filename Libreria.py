import time
import os

# --------------------------Seccion de Menus y partes Graficas de bajo nivel-------------------------------------------


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


def error():
    print("  _____                                  _ ")
    print(" | ____|  _ __   _ __    ___    _ __    | |")
    print(" |  _|   | '__| | '__|  / _ \  | '__|   | |")
    print(" | |___  | |    | |    | (_) | | |      |_|")
    print(" |_____| |_|    |_|     \___/  |_|      (_)")
    print ("\n\n")


# ---------Fin de la seccion  de Menus y partes Graficas de bajo nivel, inicio de funciones y procedimientos-----------


# Esta funcion se encarga calcular los dias nesesarios para que un caracol subaun arbol
# Param@ alutra, subida,bajada
# return@ dias que tarda
def calcular_dias_que_tarda(altura, subida, bajada):
    # Evaluar primero si las condiciones nesesarias para que no se cicle se cumplan
    while altura < 0 or subida < 0 or bajada < 0 or subida <= bajada:
        os.system("cls")
        error()
        # En caso de que si, imprimir un mensaje y volver a pedir los datos

        print("Tu datos no pueden ser 0 ni tampoco o el valor de lo que bao mayor o igual a lo que sube "
              "mas de lo que baja\n\n")
        altura = input("Dame la altura en metros del arbol: ")
        subida = input("Dame los metros que sube por dia: ")
        bajada = input("Dame los metros que baja por noche: ")
    dias_que_tarda = 0   # Inicializar los dias que se tardan
    # Este axuliliar nos ayudara a saber los metros que faltan por recorrer
    aux = altura - subida
    while aux >= 0:
        # Repefi hasta que aux sea menor a cero
        altura = (altura - subida) + bajada   # calcular altura segun los daots
        dias_que_tarda = dias_que_tarda + 1
        aux = altura - subida

    return dias_que_tarda
