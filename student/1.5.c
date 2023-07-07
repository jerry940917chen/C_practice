#include<stdio.h>
#include <math.h>
int main(void)
{
	int i;
    int s=0,z=0;
	for (i=1;i<11;i++)
		{
            s=pow(i,i);
            z=s+z;
        }
    printf("%d\n",z);

    return 0;
} 




