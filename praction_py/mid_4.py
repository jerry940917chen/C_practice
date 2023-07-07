import random
from decimal import Decimal
R=0
T=0
x=0
while True:
    a=random.randint(1,10)
    print(a)

    if R==12.3 and T==12.3:
        print("平手")
        break
    elif R>=12.3:
        print("兔子贏")
        break
    elif T>=12.3:
        print("烏龜贏")
        break
    elif a%2==0:
        T+=Decimal('0.3')
        x+=1
        print(R)
    else:
        R+=Decimal('1.2')
        T+=Decimal('0.3')
        x+=1
    print("第",x,"回合","兔子=",R,"烏龜=",T)