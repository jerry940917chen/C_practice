#include <stdio.h>

int main() 
{
    int n;
    double pi=0.0,sign=1.0;
    printf("請輸入計算圓周率的項數: ");
    scanf("%d",&n);

    for (int i=1;i<=n;i+=2) {
        pi+=sign/i;
        sign=-sign;
    }

    double result=4*pi;
    printf("圓周率的值為: %lf",result);
    return 0;
}
/*
#include <stdio.h>
int main()
{
    int x;
    double a=0,c=0;

    //為甚麼一定要空格
    printf("請輸入: ");
    scanf("%d",&x);
    for (int i=3;i<x;i+=4) {
        a-=1.0/i+a;
    }
    for (int i=5;i<=x;i+4) {
        c+=1.0/i;
    }
    double b=4*(1+a+c);
    printf("%f",b);
    
    return 0;


}
*/

