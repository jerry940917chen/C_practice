num = int(input("金字塔層數: "))

for i in range(num):
    print(" "*(num-i-1) + "*"*(2*i+1))
    #print(i)