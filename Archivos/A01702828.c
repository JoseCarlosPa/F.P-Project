/**
*
*@Author Jose Carlos Pacheco Sanchez
*@Matriucla A01702828
*
*Laboratorio No.12
**/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>
#define ESC 27
#include "A01702828_LIB.h"

int main()
{

    int opcion=0;
    do
    {
        menu(); // se manda llamar el menu
        scanf("%i*c",&opcion); //Leer la y almacenar en opcion

        system("cls");
        switch(opcion)
        {
        //Seleccion de opcion
        case 1:
        {
            char oracion[51];
            int i;
            //repetir y llamar el procesos 5 veces leeyendo tambien la oracion
            for(i=0; i<5; i++)
            {
                fflush(stdin);
                gets(oracion);
                escribir_en_archivo(oracion);
            }

        }//LLave case 1
        break;
        case 2:
        {
            printf("Cuantos alumnos desea almacenar?\n");
            int numero_alumnos;
            //leer primero el numero de alumnos y aparitr de ahi repetir el proceso hasta que se igual al numero de alumnos
            scanf("%i*c",&numero_alumnos);
            int i;
            for(i=0; i<numero_alumnos; i++)
            {
                //Llamar proceso
                escribir_con_formato();
            }
        }//llaves case 2
        break;
        case 3:
        {
            time_t tiempo = time(0);
            struct tm *tlocal = localtime(&tiempo);
            char output[128];
            strftime(output,128,"%d/%m/%y",tlocal);
            char oracion[51];
            //Inicaliuzar variables y oraciones
            int tecla,i=1;
            printf("Usa la Tecla ESC para termina.. \n");
            do
            {
                printf("Escribe una oracion (%s) %i: ",output,i);
                //Uso de flush para evitar problemas con espacios
                fflush(stdin);
                gets(oracion); //En oraicon guardar la oracion y mandarla al prodeso escribir_en_bitacora
                escribir_en_bitacora(oracion);
                i++; //Contador que te permite saber en que numero deoraicon estas
            }
            while((tecla = getch()) !=ESC);  //Con la funcion getch leer el teclaod hasta que el valor de esc == 27 aparezca terminara el rpograma

        }//llaves case 3
        break;
        case 4:
        {
            char oracion[20];
            printf("Escribe un mensaje: \n");
            fflush(stdin);
            gets(oracion);
            //LLamar el proceso esconde_en_archivo
            esconde_en_archivo(oracion);
            //Inicar el archivo para guardar el mensaje que se quiere encripatar
            FILE *archivo=fopen("Mensaje Secreto.txt","a");
            fprintf(archivo,"%s\n",oracion);
            fclose(archivo); //cerar el archivo

        }//llave case 4
        break;
        case 5:
        {
            char nombre[20];
            fflush(stdin);
            printf("Escribe el nombre de tu archivo: \n");
            gets(nombre);
            mostrar_archivo(nombre);
        }//llave case 5
        break;
        case 6:
        {
            //Se ingresara el nombre que no tenga mas de 20 caracteres
            char nombre[20];
            printf("Ingrese El nombre del archivo junto su terminacion (.txt)(otro):\n");
            //stdin para fucion gets
            fflush(stdin);
            gets(nombre);
            printf("El numero de consonantes en el archivo %s es de  %i\n\n",nombre,cuenta_consonantes(nombre));

            system("Pause");

        }//llave case 6
        break;
        case 7:
        {
            //llamamos procediumiento leer con formato
            leer_con_formato();
        }//LLave case 7
        break;
        case 8:
        {
            //llamar enceuntra en archivo que regresara el archivo secreto a sus estado normal
            encuentra_en_archivo();

        }//llave case 8
        break;
        case 9:
        {
            //Una nombre de no mas de 20
            char nombre[20];
            printf("Programa abierto: \n");
            //nombre del archivo
            printf("Ingrese El nombre de su archivo junto su terminacion (.txt)(otro):\n");
            fflush(stdin);
            gets(nombre);
            //llamar procedimeintro
            escribir_copia_mostar(nombre);


            system("Pause");
        }//llave case 5
        break;
        }//Llave switch
    }
    while(opcion!=10);
    return 0;
}
