#include <stdio.h>

int main() {
    int num = 0, res;
    scanf("%d", &num);

    for (int i=1; i<=10; i++)
    {
        printf("%d x %d = %d\n",i,num,num*i);
    }
}