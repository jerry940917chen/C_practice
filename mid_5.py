import math
x1,y1 = map(int,input().split(','))
x2,y2 = map(int,input().split(','))
x3,y3 = map(int,input().split(','))
a=((x3-x2)**2+(y3-y2)**2)**0.5
b=((x2-x1)**2+(y2-y1)**2)**0.5
c=((x1-x3)**2+(y1-y3)**2)**0.5
if a+b>c and b+c>a and c+a>b:
    print(a+b+c)
    s = (a + b + c) / 2
    abc=(s*(s-a)*(s-b)*(s-c))**0.5
    print(math.degrees(math.atan2(a, b)))
    print(math.degrees(math.atan2(a, b)))
    print(math.degrees(math.atan2(a, b)))
    r=abc/s
    ll=math.pi * r ** 2
    print(ll)
else:
    print('0')
'''
11 // 返回三角形的周长。
12 // 对于任何错误，返回<0
13 double get_perimeter(void);

15 // 返回三角形的面积。
16 // 对于任何错误，返回<0
17 double get_area(void);

19 // 获取三个角度的度数（0-360）
20 // 对于任何错误，返回<0
21 double get_degree_1(void);
22 double get_degree_2(void);
23 double get_degree_3(void);

24 // 三角形的内切圆是可以包含在三角形中的最大圆。
25 // 返回给定三角形内切圆的面积。
'''