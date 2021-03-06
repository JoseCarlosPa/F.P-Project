# coding=utf-8
"""/**
*Author: Jose Carlos Pacheco Sanchez
*Start Date: April 12 2018
*Finish Date: April 27 2018
*ID: A01702828
*School: ITESM (Qro.Mexico)
*
*
*Developed on Pycharm v.2017.3 with python 2.7
**/"""

# Inicio de Libriras y docuemntos aparte


import os  # Libreria para usar funciones de windows, se cambia si fueran MAC
import Libreria
import time
from msvcrt import getch
# Fin de las librerias


def main():
    opcion = 0  # Iniciar opcion en 0 para que mientras no sea 5 se repita
    # Ejecutar hasta colocar la opcion 7 que manda terminar el programa
    while opcion != 7:
        os.system("cls")
        Libreria.menu_principal()  # Mostrar menu
        opcion = Libreria.lee_si_es_nuemero()
        # Programa numero uno
        if opcion == 1:
            os.system("cls")
            print('Usted entro a programa en Python: ')
            # LLamamos la funcion procedimiento de cargado que mostrara una animacion con asteriscos

            Libreria.pantalla_carga()
            print("\n")
            os.system("PAUSE")
            os.system("cls")

            # Inicia programa numero uno, descripcion del problema

            print "\n Un caracol decidio subir a un arbol de 15 m de altura. "\
                "Durante cada dia tenia tiempo de subir 5 m pero mientras dormia por la noche, bajaba 4 m. "
            print" Al cabo de cuantos dias llegara a la cima del arbol?\n\n "
            print("En base estos datos genera un programa que calcule los dias dependiendo de los datos")
            print "Ingresa los datos para calcular el tiempo estimdao:\n\n"

            # Pedir los valores

            altura_arbol = input("Dame la altura en metros del arbol: ")
            metros_subidos = input("Dame los metros que sube por dia: ")
            metros_baja = input("Dame los metros que baja por noche: ")

            # llamar funcion y almacenar en dias

            dias = Libreria.calcular_dias_que_tarda(altura_arbol, metros_subidos, metros_baja)
            print("\n\n\n")
            Libreria.resultado()

            # Imprimir resltados
            print "\n\nTarda ", dias, "dias en subir el arbol"

            os.system("PAUSE")
        elif opcion == 2:
            # Programa numero dos leer en la terminal el codigo del programa hecho en c
            Libreria.pantalla_carga()
            print("\n")
            os.system("PAUSE")
            os.system("cls")
            # llamar al archivo
            print("Usted entro a Archivo en c")
            archivo = open("Archivos/Programa_c.c", "r")
            for linea in archivo.readlines():
                print linea
            # Cerrar archivo
            archivo.close()
            os.system("PAUSE")
        # Opcion para salir o terminar el programa
        elif opcion == 3:
            # Por medio de comando y libreria os, llamar y ejecutar el archivo correspondiente
            os.system("start Archivos/Programa_c.exe -p1 datos")
        elif opcion == 4:
            # Visualizar el laboratorio No.12 hecho en c
            print("\n")
            os.system("PAUSE")
            os.system("cls")
            opcion_lab = 0
            # Repetiremos hasta que lab sea igual a 5
            while opcion_lab != 5:
                os.system("cls")
                # Llamanod librerias
                Libreria.menu_laboratorio()
                opcion_lab = Libreria.lee_si_es_nuemero()
                os.system("cls")
                if opcion_lab == 1:
                    # Repetir 5 veces dando una oracion y llamando el procedimeinto para guardar en archivo
                    for i in range(0, 5):
                        oracion = raw_input("Dame una oracion")
                        Libreria.escribir_en_archivo(oracion)
                    os.system("Pause")
                elif opcion_lab == 2:
                    # Pedir numero de veces que se repetira
                    numero = input("Cuantos alumnos desea almacenar?")
                    for i in range(0, numero):
                        Libreria.escribir_con_formato()
                    os.system("Pause")
                elif opcion_lab == 3:
                    # Hasta que el valor sea esc se repetria y agregara la fecha
                    c = getch()
                    while c != '\x1b':
                        oracion = raw_input("Dame algo que quieras escribir: ")
                        # Con la libreria time agregar dia mes y año
                        oracion = (time.strftime("%d/%m/%y") + ": " + oracion)
                        c = getch()
                        Libreria.escribir_en_bitacora(oracion)
                    os.system("Pause")

                elif opcion_lab == 4:
                    # Pedir un mensaje a ecnripatr y guardar en un archivo
                    oracion = raw_input("Dame una Mensaje que queiras esncriptar: ")
                    print "Texto Cifrado: " + Libreria.encriptar_mensaje(oracion)
                    mensaje = Libreria.encriptar_mensaje(oracion)
                    archivo = open("Mensaje_secreto.txt", "a")
                    archivo.write("\n" + mensaje)
                    archivo.close()
                    os.system("Pause")

                elif opcion_lab == 5:
                    # No hace nada, sale del menu laoratorio
                    print "Adios"

        elif opcion == 5:
            # Programa numero dos leer en la terminal el codigo del programa hecho en c
            Libreria.pantalla_carga()
            print("\n")
            os.system("PAUSE")
            os.system("cls")
            # llamar al archivo
            print("Usted entro a Archivo en c")
            archivo = open("Archivos/A01702828.c", "r")
            for linea in archivo.readlines():
                print linea
            # Cerrar archivo
            archivo.close()
            os.system("PAUSE")
        elif opcion == 6:
            # Por medio de comando y libreria os, llamar y ejecutar el archivo correspondiente
            os.system("start Archivos/A01702828.exe -p1 datos")
        elif opcion == 7:
            Libreria.rombo()
            os.system("PAUSE")
            main()
        elif opcion == 8:
            # Leery linea por linea e imprimir en terinar el programa c 2
            print("Usted entro a Archivo en c")
            archivo = open("Archivos/Programa_en_c_2.c", "r")
            for linea in archivo.readlines():
                print linea
            # Cerrar archivo
            archivo.close()
            os.system("PAUSE")
        elif opcion == 9:
            # Por medio de comando y libreria os, llamar y ejecutar el archivo correspondiente
            os.system("start Archivos/Programa_en_c_2.exe -p1 datos")
        elif opcion == 10:
            exit(1)


Libreria.bienvenido()
os.system("Pause")
main()
