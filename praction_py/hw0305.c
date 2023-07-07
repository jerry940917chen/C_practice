#include"logic.h"
#include"smallten.h"
#include<stdio.h>
#include<stdint.h>
extern bool cOut, tmpS, tmpC;
extern bool z0, z1, z2, z3, z4, z5, z6, z7;

void multiplier(bool x0, bool x1, bool x2, bool x3,bool y0, bool y1, bool y2, bool y3){
    z0=andGate(x0,y0);
    z1=halfAdder(andGate(x1,y0),andGate(x0,y1));
    z2=fullAdder(andGate(x2,y0),andGate(x1,y1),cOut);
    z3=fullAdder(andGate(x3,y0),andGate(x2,y1),cOut);
    z4=halfAdder(andGate(x3,y1),cOut);
    tmpS=cOut;
    z2=halfAdder(z2,andGate(y2,x0));
    z3=fullAdder(andGate(x1,y2),z3,cOut);
    z4=fullAdder(andGate(x2,y2),z4,cOut);
    z5=fullAdder(andGate(x3,y2),tmpS,cOut);
    tmpC=cOut;
    z3=halfAdder(andGate(x0,y3),z3);
    z4=fullAdder(andGate(x1,y3),z4,cOut);
    z5=fullAdder(andGate(x2,y3),z5,cOut);
    z6=fullAdder(andGate(x3,y3),tmpC,cOut);
    z7=cOut;

}
void decimal(int32_t a,int32_t b){
    bool X0,X1,X2,X3,Y0,Y1,Y2,Y3;
    int32_t sum1=0,sum2=0,sum3=0;
    X0=a%10;
    a/=10;
    X1=a%10;
    a/=10;
    X2=a%10;
    a/=10;
    X3=a%10;
    Y0=b%10;
    b/=10;
    Y1=b%10;
    b/=10;
    Y2=b%10;
    b/=10;
    Y3=b%10;
    sum1=X3*8+X2*4+X1*2+X0;
    sum2=Y3*8+Y2*4+Y1*2+Y0;
    printf("A = %d%d%d%d (2) = %d (10)\n",X3,X2,X1,X0,sum1);
    printf("B = %d%d%d%d (2) = %d (10)\n",Y3,Y2,Y1,Y0,sum2);
    multiplier(X0,X1,X2,X3,Y0,Y1,Y2,Y3);
    sum3=z7*128+z6*64+z5*32+z4*16+z3*8+z2*4+z1*2+z0;
    printf("A x B = %d * %d = %d%d%d%d%d%d%d%d (2) = %d (10)",sum1,sum2,z7,z6,z5,z4,z3,z2,z1,z0,sum3);
}

bool check(int32_t a){
    if(a>1111)return 1;
    for(int i=4;i>0;i--){
        if(a%10==0||a%10==1)a/=10;
        else{
            return 1;
        }
    }
    return 0;
}

int main(){
    int32_t input1=0,input2=0;
    communicate();
    printf("Please enter the first number (A) in binary: ");
    scanf("%d",&input1);
    if(check(input1)){
        printf("Invaild input!");
        return 0;
    }
    printf("Please enter the second number (B) in binary: ");
    scanf("%d",&input2);
    if(check(input2)){
        printf("Invaild input!");
        return 0;
    }
    decimal(input1,input2);
}