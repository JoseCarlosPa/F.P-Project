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


# Fin de las librerias


def main():
    opcion = 0  # Iniciar opcion en 0 para que mientras no sea 5 se repita
    # Ejecutar hasta colocar la opcion 7 que manda terminar el programa
    while opcion != 7:
        os.system("cls")
        Libreria.menu_principal()  # Mostrar menu

        opcion = input("Ingresa La opcion que deseas: ")
        contador = 0  # Contador que nos sirve para lanzar un mensaje de ayuda a los 4 intentos de fallo

        while opcion >= 4 or opcion <= 0 or opcion % 1 != 0:
            # Validacion de la respuesta ingresada si no se cumple entrara hasta que sea valido
            opcion = input("Porfavor ingresa un numero valido: ")
            contador = contador + 1  # por cada ciclo el contador aumentara en 1

            if contador >= 3:
                # Despliegue de un mensaje cuando contador es mayor o igual a tres
                print "\n\nLos rangos para poder ingresar a una opcion son de 1 al 4,"
                print "no pueden ser caracteres, numeros negativos, "
                print "tener punto decimal o ser algun tipo de simbolo "
                print "debera ser  1,2,3 o 4\n\n"
                contador = 0
        # Programa numero uno
        if opcion == 1:
            os.system("cls")
            print('Usted entro a programa en Python: ')
            # LLamamos la funcion procedimiento de cargado que mostrara una animacion con asteriscos
            Libreria.pantalla_carga()
            os.system("PAUSE")
            os.system("cls")
            # Inicia programa numero uno
            print "\n Un caracol decidió subir a un arbol de 15 m de altura. "
            print"Durante cada dia tenía tiempo de subir 5 m; "
            print" pero mientras dormía por la noche, bajaba 4 m. "
            print" Al cabo de cuántos dias llegará a la cima del arbol?\n "
            print("En base estos datos genera un programa que calcule los dias dependiendo de los datos")
            print "Ingresa los datos para calcular el tiempo estimdao:"

            altura_arbol = input("Dame la altura del arbol: ")
            metros_subidos = input("Dame los metros que sube por dia: ")
            metros_baja = input("Dame los metros que baja por noche: ")

            print "Tarda ", Libreria.calcular_dias_que_tarda(altura_arbol, metros_subidos, metros_baja), "Dias en subir el arbol"

            os.system("PAUSE")
        elif opcion == 2:
            # Programa numero dos
            os.system("cls")
            print("Usted entro a Archivo en c")
        # Opcion para salir o terminar el programa
        elif opcion == 7:
            exit(1)


Libreria.bienvenido()
os.system("Pause")
main()
