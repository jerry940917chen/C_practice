year = int(input("請輸入出生年份："))

zodiac = year % 12
print(zodiac)
if zodiac == 0:
    print("你的生肖是猴")
elif zodiac == 1:
    print("你的生肖是雞")
elif zodiac == 2:
    print("你的生肖是狗")
elif zodiac == 3:
    print("你的生肖是豬")
elif zodiac == 4:
    print("你的生肖是鼠")
elif zodiac == 5:
    print("你的生肖是牛")
elif zodiac == 6:
    print("你的生肖是虎")
elif zodiac == 7:
    print("你的生肖是兔")
elif zodiac == 8:
    print("你的生肖是龍")
elif zodiac == 9:
    print("你的生肖是蛇")
elif zodiac == 10:
    print("你的生肖是馬")
else:
    print("你的生肖是羊")