#include <stdint.h> 
#include <stdio.h>  

uint32_t ui = 0;
uint16_t us = 0;
int32_t si = -1;
int main() 
{
    int64_t r1 = ui + si;
    int64_t r2 = us + si;
    printf("%ld %ld\n", r1, r2);
}