#include <stdio.h>

int main() {
    int n,i,j,is_prime;

    printf("請輸入一個正整數：");
    scanf("%d",&n);

    // 遍歷2到n之間的所有數字，判斷是否為質數
    for (i=2; i<=n;i++) {
        is_prime = 1; // 假設i是質數
        for (j=2;j<i;j++)
        {
            if (i%j==0) 
            {
                // 如果i能被任何小於i的數整除，則i不是質數
                is_prime=0;
                break;
            }
        }
        // 如果i是質數，則列印出來
        if (is_prime) 
        {
            printf("%d",i);
        }
    }
    return 0;
}