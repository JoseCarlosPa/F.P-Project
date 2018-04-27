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

import os
import Libreria


def main():
    opcion = 0  # Iniciar opcion en 0 para que mientras no sea 5 se repita

    while opcion != 5:
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

        # En todos los casos se agrego una variable llamada espera, tiene como uso copiar el system pause en c

        if opcion == 1:
            # Programa numero uno
            os.system("cls")
            print("Usted entro a programa en Python: ")
            Libreria.cargando()
        elif opcion == 2:
            # Programa numero dos
            os.system("cls")
            print("Usted entro a Archivo en c")


print("Bienvenido al maravilloso mundo de python\n\n")
os.system("Pause")
main()
