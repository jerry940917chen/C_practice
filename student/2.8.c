#include <stdio.h>

int main() {
    int a, b, r;

    printf("請輸入第一個數字：");
    scanf("%d", &a);
    printf("請輸入第二個數字：");
    scanf("%d", &b);
    while (b != 0)
    {
        r=a%b;
        a=b;
        b=r;
    }
    printf("最大公因數為：%d\n",a);
    return 0;
}