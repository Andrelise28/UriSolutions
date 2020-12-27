#include<stdio.h>

int main()
{
    float nota1,nota2,nota3,total,media;
    int i,quantidadeNotas;

    scanf("%d",&quantidadeNotas);

    for(i=1;i<=quantidadeNotas;i++)
    {
        scanf("%f%f%f",&nota1,&nota2,&nota3);
        total=(nota1*2+nota2*3+nota3*5)/10;
        printf("%.1f\n",total);
    }
    return 0;
}