'''
a=[]
z=0
x=int(input())
for i in range(7,-1,-1):
    if x%2==0:
        if x>=2**i:
            x=x-2**i
            a.append(1)
        else:
            a.append(0)
for a in range(4):
    if a[i] != a[7-i]:
        break
    else:
        z+=1
if z==4:
    print('1')
else:
    print('0')
'''
a=[]

x=int(input())
a = bin(x)[2:] # 去掉前綴'0b'
a = "{:0>8}".format(a)
print(a) # 將10進位轉換為2進位
if a == a[::-1]: # 檢查是否為回文數字
    print('1')
else:
    print('0')
