#include <stdio.h>
#include <math.h>
#include "myfunc.h"

int main() {
    int32_t a, b, c;
    double x, m, n, t;

    printf("a,b,c: ");
    scanf("%d %d %d", &a, &b, &c);

    // 設置二次函數
    int32_t setup_res = setup(a, b, c);
    if (setup_res == -1) {
    printf("不能是0\n");
    return 1;
    }

    // 給定點計算
    printf("輸入一個x值: ");
    scanf("%lf", &x);
    printf("f(%.2lf) = %.2lf\n", x, value(x));

    // 計算區間內的函數最小值
    printf("輸入區間的端點: ");
    scanf("%lf %lf", &m, &n);
    printf("在[%.2lf, %.2lf]範圍內函數的最小值是 %.2lf\n", m, n, min(m, n));

    // 計算區間內的函數最大值
    printf("在[%.2lf, %.2lf]範圍內函數的最大值是 %.2lf\n", m, n, max(m, n));

    // 計算在指定點的切線斜率
    printf("輸入一個點t: ");
    scanf("%lf", &t);
    printf("在x = %.2lf 的切線斜率為 %.2lf\n", t, slope(t));

    return 0;
}