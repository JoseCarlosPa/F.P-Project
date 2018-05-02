

#include <stdio.h>
#include <stdlib.h>


// Funciones
void menu(){
    printf("\t\t|--------------------------------------------------|\n");
    printf("\t\t|------------Despacahdora de bebidas---------------|\n");
    printf("\t\t|--------------------------------------------------|\n\n");
}
void menu_bebidas(){
    printf("\t\t |Bebida      \tBoton\t\tPrecio|\n\n");
    printf("\t\t |Coca-cola   \t-1-  \t\t12$   |\n");
    printf("\t\t |Sprite      \t-2-  \t\t10$   |\n");
    printf("\t\t |Fanta       \t-3-  \t\t11$   |\n");
    printf("\t\t |sidral      \t-4-  \t\t10$   |\n");
    printf("\t\t |Agua        \t-5-  \t\t12$   |\n");
}

int cambio(int ingreso){

}
int main(){
    int salida=0, opcion=0;
    int cocas=5,sprite=5,fanta=5,sidral=5,agua=5;
    do{
            system("cls");
            menu();
            menu_bebidas();
            printf("\n\t\tProfavor elige tu bebida: ");
            scanf("%i*c",&opcion);
            switch(opcion){
            case 1:
                {
                    int pago=0;
                    printf("Has elegido Coca-cola , serian 12$ pesos\n");
                    printf("\nIngrese el efectivo: ");
                    scanf("%i*c",&pago);
                    while(pago<12 || pago%1!=0){
                        if (pago<12){
                            int total=0,opcion2=0;
                            total = 12-pago;
                            printf("Le hacen fala %i peso  ",total);
                            printf("\nDesea ingresar efectivo(1) o cancelar(2) ");
                            scanf("%i*c",&opcion2);
                            if (opcion2== 1){
                                int pago2=0;
                                printf("\nIngrese el efectivo: ");
                                scanf("%i*c",&pago2);
                                total= total-pago2;
                                if (total<0){
                                    int cambio =0;
                                    cambio= total*-1;
                                    printf("Su cambio es de %i$ \n",cambio);
                                }
                            }else{

                                printf("Cancelando...");
                                printf("Regresando dinero: %i$ pesos\n\n",pago);
                                system("PAUSE");
                                system("cls");
                                goto terminar;
                            }
                        }
                    }
                }// llave case1
                break;
            case 2:
                {

                }// llave case2
                break;
            case 3:
                {

                }// llave case3
                break;
            case 4:
                {

                }// llave case4
                break;
            case 5:
                {

                }// llave case5
                break;

            }
            printf("\n");
            system("PAUSE");
            terminar:
            printf("Desea otra cosa , si(1) no (2)");
            scanf("%i*c",&salida);



    }while (salida!=2);


}





