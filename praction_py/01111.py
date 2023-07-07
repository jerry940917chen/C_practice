x = [3,6,2,7,3,4,1] # 7
count =0
for i in range(len(x)):
    for j in range(len(x)-i-1):
        count+=1
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
        print(x)
    print('=================================')

print(count)
