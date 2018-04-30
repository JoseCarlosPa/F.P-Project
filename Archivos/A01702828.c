/**
*
*@Author Jose Carlos Pacheco Sanchez
*@Matriucla A01702828
*
*Laboratorio No.11
**/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>
#define ESC 27

//Funciones

/**
*Procedimiento para desplegar el menu principal
**/
    void menu(){
        system("cls");
        printf("-----------------------------------\n");
        printf("               MENU\n");
        printf("-----------------------------------\n");
        printf("1. Escribe en Archivo: \n");
        printf("2. Guardar datos de alumnos: \n");
        printf("3. Escribir en bitacora:\n");
        printf("4. Esconde en archivo:\n");
        printf("5. Programa abierto:\n");
        printf("6. Salir:\n");
        printf("-----------------------------------\n");

    }

    /**
*Procedimiento donde escribe 5 oraciones de al menos 50 caraceteres
*
**/
    void escribir_copia(char nombre[]){
        char oracion[50];
        FILE*archivo=fopen(nombre,"a");
        printf("\n\nEscriba la oracion que desee agregar a este documento:\n");
        fflush(stdin);
        gets(oracion);
        fprintf(archivo,"%s\n",oracion);
        fclose(archivo);

    }

/**
*Procedimiento donde escribe 5 oraciones de al menos 50 caraceteres
*
**/
    void escribir_en_archivo(char nombre_archivo[]){
        FILE *archivo=fopen("Ejer1.txt","a");
        fprintf(archivo,"%s\n",nombre_archivo);
        fclose(archivo);

    }

/**
*Procedimiento donde escribe con un formato especifico las oraciones
*
**/
void escribir_con_formato (){
        system("cls");
        //Iniciar el archivo con el nombre califica
        FILE*archivo=fopen("califica.txt","a");
            char oracion[51];
            printf("\nEscriba el nombre del alumno:");
            //Usar la funcion fflsuh para evitar errores en espacios
                fflush(stdin);
                //USar gets para cputarar la oraicon
                    gets(oracion);
                fprintf(archivo, "%s,",oracion);
            printf("\nEscirba la carrea del alumno:");
            //Se reptire
                fflush(stdin);
                    gets(oracion);
                fprintf(archivo, "%s,",oracion);
            printf("\nEscirba la calificacion del alumno:");
            //Se repite
                fflush(stdin);
                    gets(oracion);
                fprintf(archivo, "%s\n",oracion);
                fprintf(archivo,"------------------------------------\n");
        fclose(archivo);


}
/**
*Procedimiento donde escribe hasta que se ponga un esc
*
**/
void escribir_en_bitacora(char nombre_archivo[]){
    FILE *archivo=fopen("Ejer3.txt","a");
    //Dependiendo de lo que reciba, escribirlo en le arhcivo
        fprintf(archivo,"%s\n",nombre_archivo);
        fclose(archivo);
}

/**
*Procedimiento donde escirbe un mensaje y este se reescribira pero con cada caracter recorrido
*
**/

//Sacar con la funcion longitu, la longitu de la cadena para poder inverirla
int longitud(char nombre_archivo[]) {

    int i;
    for (i=0; nombre_archivo[i] != '\0'; i++);
    return i;
}
//A partir de la funcion longitud usar ...
void esconde_en_archivo(char nombre_archivo[]){
    int i;
    //Repetir hasta que la cadena termine y reccorrer en la posision X,Y 1 para que sea la sigueinte legtra
     for (i=0; i < longitud(nombre_archivo); i++) {
        nombre_archivo[i] = nombre_archivo[i] + 1;
    }
}
int main(){

    int opcion=0;
        do{
                menu(); // se manda llamar el menu
                scanf("%i*c",&opcion); //Leer la y almacenar en opcion

            system("cls");
            switch(opcion){
                //Seleccion de opcion
                case 1:{
                    char oracion[51];
                    int i;
                    //repetir y llamar el procesos 5 veces leeyendo tambien la oracion
                    for(i=0;i<5;i++){
                    fflush(stdin);
                    gets(oracion);
                    escribir_en_archivo(oracion);
                    }

                }//LLave case 1
                break;
                case 2:{
                    printf("Cuantos alumnos desea almacenar?\n");
                    int numero_alumnos;
                    //leer primero el numero de alumnos y aparitr de ahi repetir el proceso hasta que se igual al numero de alumnos
                    scanf("%i*c",&numero_alumnos);
                    int i;
                    for(i=0;i<numero_alumnos;i++){
                    //Llamar proceso
                    escribir_con_formato();
                    }
                }//llaves case 2
                break;
                case 3:{
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
                    }while((tecla = getch()) !=ESC); //Con la funcion getch leer el teclaod hasta que el valor de esc == 27 aparezca terminara el rpograma

                }//llaves case 3
                break;
                case 4:{
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
                case 5:{
                    char nombre[20];
                    printf("Programa abierto: \n");
                    printf("Ingrese El nombre de su archivo junto su terminacion (.txt)(otro):\n");
                    fflush(stdin);
                    gets(nombre);
                    escribir_copia(nombre);


                    system("Pause");
                }//llave case 5
                break;
            }//Llave switch
        }while(opcion!=6);


return 0;
}//Final


