/*
int32_t array01[5]={5}
int32_t array02[5]={1,2,3,4,5}
int32_t array03[]={1,2,3,4,5,6,7}
int32_t array04[SIZE_OF_ARRAY]={1,2,3,4,5,6,7}
int32_t array01[]={5}
*/

#include <stdio.h>

void siri_garden_bubble_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            // 比較相鄰兩個元素，如果前面的元素大於後面的元素，則交換它們
            if (arr[j] > arr[j + 1]) {
                // 使用加法和減法進行元素交換，不使用額外的區域變數
                arr[j] = arr[j] + arr[j + 1];
                arr[j + 1] = arr[j] - arr[j + 1];
                arr[j] = arr[j] - arr[j + 1];
            }
        }
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("排序前的數組：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    siri_garden_bubble_sort(arr, n);

    printf("\n排序後的數組：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}