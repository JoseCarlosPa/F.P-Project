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
    print ("|7. Programa en python 2            |")
    print ("|8. programa en c                   |")
    print ("|9. Ejecutar e c                    |")
    print ("|10. Salir                           |")
    print ("|-----------------------------------|")


def menu_laboratorio():

    print("-----------------------------------\n")
    print("               MENU\n")
    print("-----------------------------------\n")
    print("1. Escribe en Archivo: \n")
    print("2. Guardar datos de alumnos: \n")
    print("3. Escribir en bitacora:\n")
    print("4. Esconde en archivo:\n")
    print("5. Programa abierto:\n")
    print("6. Salir:\n")
    print("-----------------------------------\n")


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

def lee_si_es_nuemero():
    # Se repetira hasta llegar al return
    while True:
        opcion = raw_input("Ingrese la Opcion deseada: ")
        try:
            # Al poner el int aseguramos que sea entero si no lo es, entra al caso esepcion y repite el ciclo
            opcion = int(opcion)
            return opcion
        except ValueError:
            print "Has ingresado una opcion no valida, intentalo otra vez por favor"\
                "las opciones validas son numeros como 1,2,3...10, no se pueden negativos , decimal o letras"

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

# Inicio funciones y procedimientos de Laboratorio 12 c a python

def escribir_en_archivo(oracion):
    archivo = open("Ejercicio1.txt","a")
    archivo.write("\n" + oracion)
    archivo.close()

def escribir_en_bitacora(oracion):
    archivo = open("Bitacora.txt","a")
    archivo.write("\n" + oracion)
    archivo.close()

def escribir_con_formato():
    archivo = open("califica.txt", "a")
    nombre = raw_input("Dame el nombre del alumno: ")
    archivo.write(nombre)
    carrera = raw_input("Dame la carrera del alumno: ")
    archivo.write(", " + carrera)
    calificaicon = raw_input("Dame la calificacion del alumno: ")
    archivo.write(", " + calificaicon + "\n")
    archivo.close()