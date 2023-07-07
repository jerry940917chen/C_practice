#a=[int(x) for x in input().split(,)]sepfloat
P1=list(map(str,(input().split(','))))    
print(P1)   
P2=list(map(str,(input().split(','))))   
P3=list(map(str,(input().split(','))))   
P4=list(map(str,(input().split(','))))   
P=list(map(str,(input().split(','))))

a=float(P1[0])
b=float(P1[1])
c=float(P3[0])
d=float(P3[1])
if  float(P1[0])+float(P3[0])==float(P2[0])+float(P4[0]) and float(P1[1])+float(P3[1])==float(P2[1])+float(P4[1]):
    x1=(a+c)/2
    y1=(b+d)/2
    x=float(P[0])
    y=float(P[1])
    m=(y-y1)/(x-x1)
    b=y-m*x
    print("y =",m,"* x +",b)
 