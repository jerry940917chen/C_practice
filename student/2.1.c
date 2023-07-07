#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char s[]="applerickjerry";
    int length=strlen(s);
    char *b=malloc(length*sizeof(char));
    //使用malloc()函数动态分配一块内存来存储去重后的字符，分配的内存大小为字符串s的长度length乘以每个字符占用的字节数（在这里是sizeof(char)，也就是1字节），即length * sizeof(char)。最后将分配的内存块的首地址赋值给指针变量b，用来存储去重后的字符。
    int i,j,k=0;
    // 删除重复字符
    for (i=0;i<length;i++) 
    {
        for (j=0;j<k;j++) 
        {
            if (b[j]==s[i]) 
            {
                break;
            }
        }
        if (j==k) 
        {
            b[k++] = s[i];
        }
    }
    // 排序字符
    for (i=0;i<k-1;i++) {
        for (j=i+1;j<k; j++) {
            if (b[i]>b[j]) 
            {
                char temp=b[i];
                b[i]=b[j];
                b[j]=temp;
            }
        }
    }
    printf("%s\n",b);
    free(b);
    //在使用malloc()函数分配内存后，需要在使用完后使用free()函数来释放内存，避免出现内存泄漏的情况
    return 0;
}