number1=list(map(int, input("A（x,y）：").split(",")))
number2=list(map(int, input("B（x,y）：").split(",")))
number3=list(map(int, input("C（x,y）：").split(",")))
print(number1)
x1=number1[0]
y1=number1[1]

x2=number2[0]
y2=number2[1]

x3=number2[0]
y3=number2[1]

if y2-y1>0:
    a=(x2-x1/y2-y1)*-1
    b=a*x3+y3
    print("y=",a,"x+",b)
else:
    print("non-existent")