'''
import time


y=[]
n=int(input()) #n is how money number
for i in range(n):
    y.append(list(map(int, input().split())))
    print(y)

t1 = time.time()
max=y[0][1]
for i in range(1,n):
    if max<y[i][1]:
        max=y[i][1]
print(max)
a=[0 for i in range(max)]
print(a)


for i in range(n):
    for j in range(y[i][0],y[i][1]):
        a[j]=1
print(a)
print(a.count(1))



t2 = time.time()
total_time =  t2 - t1
print(total_time)
'''
#include <stdio.h>
#include <stdlib.h>

#define ROW 2
#define COL 3

int main()
{
    int **arr = (int **)malloc(sizeof(int *) * ROW);

    for(int i = 0; i < ROW; i++)
    {
        *(arr + i) = (int *)malloc(sizeof(int) * COL);
    }

    int count = 0;

    for(int i = 0; i < ROW; i++)
    {
        for(int j = 0; j < COL; j++)
        {
            *(*(arr + i) + j) = count++;
        }
    }

    for(int i = 0; i < ROW; i++)
    {
        for(int j = 0; j < COL; j++)
        {
            printf("%d ", *(*(arr + i) + j));
        }

        printf("\\n");
    }

    for(int i = 0; i < ROW; i++)
    {
        free(*(arr + i));
    }

    free(arr);

    return 0;
}