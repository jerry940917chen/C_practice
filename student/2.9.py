def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a = int(input("請輸入第一個數字："))
b = int(input("請輸入第二個數字："))

lcm = (a*b) // gcd(a,b)

print("最小公倍數為：",lcm)