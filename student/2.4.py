n=int(input("請輸入計算圓周率的項數: "))

pi=0
sign=1
for i in range(1,n+1,2):
    pi+=sign/i
    sign=-sign
    a=4*pi
print("圓周率的值為: ",a)

