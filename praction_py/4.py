'''
level = 50
atk = 100
defense = 80
power = 70
weather = 1
stab = 1
type_effectiveness = 2
status_effect = 1
terrain_effect = 1

if weather==1:
    water=water*0.5
    fire=fire*2
elif weather==2:
    water=water*2
    fire=fire*0.5

if atk=='water':
    if atk=='water' or atk=='grass' or atk=='dragon':
        atk=atk*0.5

if atk=='fire':
    if atk=='water' or atk=='fire' or atk=='rock' or atk=='dragon':
        atk=atk*0.5
    elif atk=='grass':
        atk=atk*2

if atk=='grass':
    if  atk=='fire' or atk=='grass' or atk=='flying' or atk=='dragon':
        atk=atk*0.5
    elif atk=='water' or atk=='rock' or atk=='ground':
        atk=atk*2

if atk=='flying':
    if  atk=='rock'  or atk=='rock':
        atk=atk*0.5
    elif atk=='grass':
        atk=atk*2

factor=weather*stab*type_effectiveness*status_effect*terrain_effect
damage=math.floor(((math.floor((level * 2 + 10) / 250) * (atk / defense) * power) + 2) * factor)
print(damage)
'''

wea = 0.5
status = 1
ter = 1
dam1 = 110
movety = 0
ttype = 6

if wea == 0.5 and ((movety == 0 and (ttype == 1 or ttype == 4 or ttype == 5)) or
                   (movety == 1 and ttype == 2) or
                   (movety == 2 and (ttype == 0 or ttype == 4 or ttype == 5)) or
                   (movety == 3 and ttype == 2) or
                   (movety == 4 and (ttype == 1 or ttype == 3)) or
                   (movety == 5 and (ttype == 1 or ttype == 4 or ttype == 6)) or
                   (movety == 6 and ttype == 5)):
    fty = 2
    fac = wea * status * ter * fty
    dam2 = (dam1 + 2) * fac
    print("Damage =", dam2)
elif ((movety == 0 and (ttype == 0 or ttype == 2 or ttype == 7)) or
      (movety == 1 and (ttype == 0 or ttype == 1 or ttype == 4 or ttype == 7)) or
      (movety == 2 and (ttype == 1 or ttype == 2 or ttype == 3 or ttype == 7)) or
      (movety == 3 and (ttype == 4 or ttype == 6)) or
      (movety == 4 and ttype == 5) or
      (movety == 6 and (ttype == 2 or ttype == 6 or ttype == 7))):
    fty = 0.5
    fac = wea * status * ter * fty
    dam2 = (dam1 + 2) * fac
    print("Damage =", dam2)
elif (movety == 5 and ttype == 3) or (movety == 6 and ttype == 5):
    print("Damage = 0")
else:
    fty = 1
    fac = wea * status * ter * fty
    dam2 = (dam1 + 2) * fac
    print("Damage =", dam2)

#297