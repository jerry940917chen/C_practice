n=int(input())

def start(n):
    if n == 10 or n == 35:
        s1 = int(input("s1"))
        s1_func(s1)
    elif n == 20 or n == 78:
        s5 = int(input("s5"))
        s5_func(s5)
    elif n == 11:
        s3 = int(input("s3"))
        s3_func(s3)
    else:
        n=int(input("start"))
        start(n)

def s1_func(n):
    if n == 12 or n == 36:
        s6 = int(input("s6"))
        s6_func(s6)
    elif n == 19:
        s2 = int(input("s2"))
        s2_func(s2)
    else:
        s1=int(input("s1"))
        s1_func(s1)
def s2_func(n):
    if n == 43:
        s2 = int(input("s2"))
        s2_func(s2)
    elif n == 99:
        final = int(input("final"))
        print(final)
    else:
        n=int(input("start"))
        start(n)

def s3_func(n):
    s4 = int(input("s4"))
    s4_func(s4)

def s4_func(n):
    s6 = int(input("s6"))
    s6_func(s6)

def s5_func(n):
    if n == 1:
        s4 = int(input("s4"))
        s4_func(s4)
    elif n == 2:
        s6 = int(input("s6"))
        s6_func(s6)
    else:
        n=int(input("start"))
        start(n)

def s6_func(n):
    if n == 108:
        final = int(input("final"))
        print(final)
    else:
        s5 = int(input("s5"))
        s5_func(s5)

start(n)
