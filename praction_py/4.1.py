'''
c=list(map(int,input() .split(',')))
p=list(map(int,input() .split(',')))
if p[2]-1==-1:
    print(int(c[0]),"X","x^",(int(p[0])-1),"+",int(c[1]),"X","x^",(int(p[1])-1))#,"+",int(c[2]),"X","x^",(int(p[2])-1))
else:
    print(int(c[0]),"X","x^",(int(p[0])-1),"+",int(c[1]),"X","x^",(int(p[1])-1),"+",int(c[2]),"X","x^",(int(p[2])-1))
'''
c = list(map(int, input().split(',')))
p = list(map(int, input().split(',')))

result = ""
for i in range(len(c)):
    for j in range(len(p)):
        if p[j] == 0:
            if j == i:
                term = str(c[i])
                if i != len(c)-1:
                    term += " + "
                result += term
        elif j == i:
            term = str(c[i]) + "x"
            if p[i] > 1:
                term += "^" + str(p[i]-1)
            if i != len(c)-1:#b如果是在最後一項就不印+號
                term += " + "
            result += term

print(result)