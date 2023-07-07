import math
n = int(input("n值"))

z=1
pi_1 = 4
pi_2 = 3
sign_1 = -1
sign_2 = 1
for j in range(n):
    for i in range(3, n*2+2, 2):
        pi_1 +=sign_1  * (4 / i)
        sign_1 *= -1
for j in range(n):
    for i in range(2, n*2+2, 2):
        pi_2 += sign_2  * (4 / (i * (i + 1) * (i + 2)))
        sign_2 *= -1

for i in range(1, n + 1):
    print(f"n = {i}:")
    print(f"Gregory-Leibniz 級數: {round(abs(pi_1))} (ddd{z})")
    z+=1
    print(f"Nilakantha 級數: {round(abs(pi_2))} (ddd{z})")