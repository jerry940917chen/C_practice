a = int(input("請輸入第一個數字："))
b = int(input("請輸入第二個數字："))
while b!=0:
    r=a%b
    a=b
    b=r
print("最大公因數：",a)