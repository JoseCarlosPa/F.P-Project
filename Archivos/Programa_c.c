/**
*
*@Author Jose Carlos Pacheco Sanchez
*@Matriucla A01702828
*
*Programa en c comparado con python - Protyecto Final
**/

#include <stdio.h>
#include <stdlib.h>

// Funciones

int dias_que_tarda_en_subir(int altura,int subida, int bajada){
        int dias_que_tarda=0;
        while(altura<0 || subida<0 || bajada<0 || subida<=bajada){
            system("cls");
            printf("Tud datos no pueden ser 0 ni tampoco el valord del mas bajo mayor a lo que sube\n\n");
            int altura=0,subida=0,bajada=0;
            printf("Dame la altura: \n");
            scanf("%i*c",&altura);
             printf("Dame la subida: \n");
            scanf("%i*c",&subida);
             printf("Dame la bajada: \n");
            scanf("%i*c",&bajada);
        }
        int aux=0;
        aux = altura - subida;
        while (aux>=0){
        altura = (altura-subida)+bajada;
        dias_que_tarda++;
        aux=altura-subida;
        }
        return dias_que_tarda;
}

//Fin funciones

int main(){
    int altura=0,subida=0,bajada=0;
    printf("EL problema del caracol, Un caracol decidio subir a un arbol de 15 m de altura. Durante cada dia tenia tiempo de subir 5 m pero mientras dormia por la noche, bajaba 4 m. \n");
            printf(" Al cabo de cuantos dias llegara a la cima del arbol?\n\n ");
            printf ("En base estos datos genera un programa que calcule los dias dependiendo de los datos\n");
            printf ("Ingresa los datos para calcular el tiempo estimdao \n");
    printf("Dame la altura: \n");
    scanf("%i*c",&altura);
    printf("Dame la subida: \n");
    scanf("%i*c",&subida);
    printf("Dame la bajada: \n");
    scanf("%i*c",&bajada);
printf("tada : %i dias\n\n",dias_que_tarda_en_subir(altura,subida,bajada));
system("Pause");
return 0;
}

