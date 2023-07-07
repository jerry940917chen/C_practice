import math
rad=0
x,y,theta=map(int,input("x, y, theta").split())

rad = math.radians(theta)

sin_theta = math.sin(rad)
cos_theta = math.cos(rad)


'''
x1= x * cos_theta - y * sin_theta
y1 = x * sin_theta + y * cos_theta
'''
x1 = round(sin_theta, 10)  # 四捨五入為10位小數
y1 = round(cos_theta, 10)
print(x1,y1)
