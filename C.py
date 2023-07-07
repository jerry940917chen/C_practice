x = list(map(int, input().split())) 
#print(x)
y = []
Z = []
p = []
for i in range(x[0]): #使用者第一位輸入隊伍數給定每隊的數值
    y.append(list(map(str, input().split())))
    y[i][2]=str(y[i][2])
#a = [[map(int, input().split()) for i in range(y)] for j in range(x)]
if str(input())=='':
    for j in range(x[0]):
        a=input() 
        if a!='':
            if 0<int(a)<=x[0]:
                Z.append(int(a))
        else:
            break
print(Z)
#if y[0][2]>=y[1][2]>=y[2][2] and y[0][1]>=y[0][1]>=y[1][2]:

for i in range(x[0]):
    for j in range(x[0]-i-1):
        if y[j][0]<y[j+1][0]:
            y[j],y[j+1]=y[j+1],y[j]

for i in range(x[0]):
    for j in range(x[0]-i-1):
        if y[j][0]==y[j+1][0] and y[j][1]>y[j+1][1]:
            y[j],y[j+1]=y[j+1],y[j]

print(y)

for i in Z:
    print(y[i-1][2])
'''
q=len(Z)
for o in range(q):
    for k in range(x[0]):
        if int(y[k][0])<=int(y[k+1][0]):
            for s in range(x[1]-1):
                if int(y[1][s])>=int(y[1][s+1]):
                    W=y[2][s]
                 

print(y)
print(W)
'''