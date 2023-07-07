#include <stdio.h>

int main() 
{
    char str[]="Hello,World!";
    int len=printf("%s",str);
    printf("\nLength: %d\n",len);
    return 0;
}