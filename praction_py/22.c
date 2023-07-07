#include <stdio.h>
#include <stdint.h>

int main()
{
    int8_t  a=0;
    int16_t b=0;
    int32_t c=65535;

    printf("&a %p\n",&a);
    printf("&b %p\n",&b);
    printf("&c %p\n",&c);

    int8_t *ptr =(int8_t *)&c;
    *ptr=0;
    printf("c:%d\n",c);
    return 0;
}