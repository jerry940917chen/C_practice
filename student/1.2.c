#include<stdio.h>
int main()
{
	int i,j;
	for (i=1;i<10;i++)
		{
			for(j=1;j<10;j++)
			{
		
				printf("%d*%d=%02d ",i,j,i*j);
			
			}
			printf("\n");
            //使程式每列印完第一行的乘法表之後，再換行
		}
	return 0;
 } 