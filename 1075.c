#include <stdio.h>

int main(){

    int numeros, valor;

    scanf("%d", &valor);
    for(numeros=1;numeros<=10000;numeros++){
        if(numeros%valor==2){
            printf("%d\n", numeros);
        }
    }
    return 0;
}