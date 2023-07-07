a = 0
b = 0
c = 0

def setup(a,b,c):
    global a, b, c
    a = int(input("a值："))
    b = int(input("b值："))
    c = int(input("c值："))
    if a == 0:
        return -1
    else:
        return 0

def value(x):
    return a*x*x + b*x + c

def min(m, n):
    if m > n:
        m, n = n, m
    if a > 0:
        return value(-(b/(2*a)))
    else:
        if value(m) < value(n):
            return value(m)
        else:
            return value(n)

def max(m, n):
    if m > n:
        m, n = n, m
    if a < 0:
        return value(-(b/(2*a)))
    else:
        if value(m) > value(n):
            return value(m)
        else:
            return value(n)

def slope(t):
    return 2*a*t + b

# 输入二次函数的係數
if setup() == -1:
    print("不能是0")
else:
    x = float(input("變量x的值："))
    print("f(x) = ", value(x))

    m = float(input("左端點m的值："))
    n = float(input("右端點n的值："))
    print("f(x)在區间[{}, {}]上的最小值{}".format(m, n, min(m, n)))
    print("f(x)在區间[{}, {}]上的最大值{}".format(m, n, max(m, n)))

    t = float(input("t的值："))
    print("f(x)在x={}的切線斜率為{}".format(t, slope(t)))