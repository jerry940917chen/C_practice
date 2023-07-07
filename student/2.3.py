x= int(input("輸入菱形大小: "))

# 上半部分
for i in range(x):
    print(" "*(x-i-1) + "*"*(2*i+1))

# 下半部分
for i in range(x-2, -1, -1):
    print(" "*(x-i-1) + "*"*(2*i+1))
    #print(i)