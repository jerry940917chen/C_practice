#include <stdio.h>

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
        //gcd是最大公因式縮寫
    }
}

int main() {
    int a, b, lcm;

    printf("請輸入第一個數字：");
    scanf("%d", &a);

    printf("請輸入第二個數字：");
    scanf("%d", &b);

    lcm = (a * b) / gcd(a, b);

    printf("最小公倍數為：%d\n", lcm);

    return 0;
}