#include <stdio.h>

int main()
{
    int num,i, posicao=0, aux=0;

    for (i=0; i<100; i++)
    {
        scanf("%d", &num);
        if (num>aux){
            aux = num;
            posicao = i+1;
        }
    }
    printf("%d\n", aux);
    printf("%d\n", posicao);
    return 0;
}