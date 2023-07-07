#include <stdio.h>

int main()
{
    int x;
    printf("菱形數: ");
    scanf( "%d" , &x);

   
    for(int i=0; i<x; i++)
    {
        for(int j=0;j<x-i-1;j++) 
        {
            printf(" ");
        }
        for(int k=0;k<2*i+1;k++) 
        {
            printf("*");
        }
        printf("\n");
    }

    for(int i=x-2;i>=0; i--)
    {
        for(int j=0;j<x-i-1;j++) 
        {
            printf(" ");
        }
        for(int k=0;k<2*i+1;k++) 
        {
            printf("*");
        }
        printf("\n");
    }
}