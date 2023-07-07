#include <stdio.h>
#include <stdint.h>

int main()
{
    int32_t a=5;


    printf("%d\n",*(&a));
    return 0;
}