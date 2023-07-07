c = lambda f, a, b, n: sum([f(a + (b - a) / n * i) * (b - a) / n for i in range(n)])
f = lambda x: x**2

a, b, n = map(int, input().split())

d = c(f, a, b, n)

print(d)