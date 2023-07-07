#include <stdio.h>

int main() {
    int year, zodiac;
    
    // 輸入出生年份
    printf("請輸入出生年份：");
    scanf("%d", &year);
    
    // 計算生肖
    zodiac = year % 12;
    
    // 顯示結果
    if (zodiac == 0) {
        printf("你的生肖是猴\n");
    } else if (zodiac == 1) {
        printf("你的生肖是雞\n");
    } else if (zodiac == 2) {
        printf("你的生肖是狗\n");
    } else if (zodiac == 3) {
        printf("你的生肖是豬\n");
    } else if (zodiac == 4) {
        printf("你的生肖是鼠\n");
    } else if (zodiac == 5) {
        printf("你的生肖是牛\n");
    } else if (zodiac == 6) {
        printf("你的生肖是虎\n");
    } else if (zodiac == 7) {
        printf("你的生肖是兔\n");
    } else if (zodiac == 8) {
        printf("你的生肖是龍\n");
    } else if (zodiac == 9) {
        printf("你的生肖是蛇\n");
    } else if (zodiac == 10) {
        printf("你的生肖是馬\n");
    } else {
        printf("你的生肖是羊\n");
    }
    
    return 0;
}

/*
#include <stdio.h>

int main() {
    int year, zodiac;
    
    // 輸入出生年份
    printf("請輸入出生年份：");
    scanf("%d", &year);
    
    // 計算生肖
    zodiac = year % 12;
    
    // 顯示結果
    switch(zodiac) {
        case 0:
            printf("你的生肖是猴\n");
            break;
        case 1:
            printf("你的生肖是雞\n");
            break;
        case 2:
            printf("你的生肖是狗\n");
            break;
        case 3:
            printf("你的生肖是豬\n");
            break;
        case 4:
            printf("你的生肖是鼠\n");
            break;
        case 5:
            printf("你的生肖是牛\n");
            break;
        case 6:
            printf("你的生肖是虎\n");
            break;
        case 7:
            printf("你的生肖是兔\n");
            break;
        case 8:
            printf("你的生肖是龍\n");
            break;
        case 9:
            printf("你的生肖是蛇\n");
            break;
        case 10:
            printf("你的生肖是馬\n");
            break;
        default:
            printf("你的生肖是羊\n");
    }
    
    return 0;
}
*/