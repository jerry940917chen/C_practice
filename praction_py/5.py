'''
x=list(map(int, input().split()))
print(x)
x.sort()
a=x[0]
b=x[1]
c=x[2]
d=x[3]
e=x[4]
many=max(x,key=x.count)
f=x.count(many)
print(f)
if  ((a>=1 or a<=52) and (b>=1 or b<=52) and (c>=1 or c<=52) and (d>=1 or d<=52) and (e>=1 or e<=52)):
    if (1<=a<=13 and 1<=b<=13 and 1<=c<=13 and 1<=d<=13 and 1<=e<=13) or (14<=a<=26 and 14<=b<=26 and 14<=c<=26 and 14<=d<=26 and 14<=e<=26) or (27<=a<=39 and 27<=b<=39 and 27<=c<=39 and 27<=d<=39 and 27<=e<=39) or (1<=a<=13 and 40<=b<=52 and 40<=c<=52 and 40<=d<=52 and 40<=e<=52):
        if int(x[4])-int(x[3])==1 and int(x[3])-int(x[2])==1 and int(x[2])-int(x[1])==1 and int(x[1])-int(x[0])==1:
            print("Straight Flush")

if f==3:
    print("Four of a kind")

if f==2:
    print("Four of a kind")


ranks = {
    14: "Ace",
    13: "King",
    12: "Queen",
    11: "Jack",
    10: "10",
    9: "9",
    8: "8",
    7: "7",
    6: "6",
    5: "5",
    4: "4",
    3: "3",
    2: "2"
}

# Encode the cards as integers from 1 to 52
a = list(map(int, input().split()))

# Sort the cards in descending order of their rank
b = sorted(a)
p=[]

a=[[1,2]]
c=sorted(p, reverse=True)
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
d0=(b[0]+13)//13
d1=(b[0]+13)//13
d2=(b[0]+13)//13
d3=(b[0]+13)//13
d4=(b[0]+13)//13
print(d0)
print(d1)
# Check for the different categories of hand
if (c[0]+5)==(c[1]+4)==(c[2]+3)==(c[3]+2)==(c[4]+1) and (d0)==(d1)==(d2)==(d3)==(d4):
    print("Straight Flush")
    
elif (c[0])==(c[1])==(c[2])==(c[3])!=(c[4]):
    print("Four of a Kind")

elif ((c[0]+5)==(c[1]+4)==(c[2]+3)and(c[3]+2)==(c[4]+1)) or ((c[0]+5)==(c[1]+4)and(c[2]+3)==(c[3]+2)==(c[4]+1)):
    print("Full house")

elif (c[0]+5)==(c[1]+4)==(c[2]+3)==(c[3]+2)==(c[4]+1):
    print("Straight**")

elif (d0)==(d1)==(d2)==(d3)==(d4):
    print("Flush**")






elif (a[0] == a[1] and a[2] == a[4]) or (a[0] == a[2] and a[3] == a[4]):
    print("Full House")
elif all(card // 13 == a[0] // 13 for card in a):
    print("Flush")
elif a[0] - a[4] == 4:
    print("Straight")
elif (a[0] == a[2] or a[1] == a[3] or a[2] == a[4]):
    print("Three of a Kind")
elif (a[0] == a[1] and a[2] == a[3]) or (a[0] == a[1] and a[3] == a[4]) or (a[1] == a[2] and a[3] == a[4]):
    print("Two Pair")
elif (a[0] == a[1] or a[1] == a[2] or a[2] == a[3] or a[3] == a[4]):
    print("One Pair")
else:
    print("High Card")
'''

'''
cards=list(map(int, input().split()))
cards.sort()
a={}
for card in cards:
    rank = (card-1)%13+1
    if rank in a:
        a[rank]+=1
    else:
        a[rank]=1

if len(a) == 2:
    for count in a.values():
        if count == 4:
            print("Four of a kind")
        elif count == 3:
            print("Full house")
elif len(a) == 3:
    for count in a.values():
        if count == 3:
            print("Three of a kind") 
        elif count == 2:
            print("Two pair")  
elif len(a) == 4:
    print("One pair")
else:
    is_flush = all(card in range(cards[0], cards[0]+13) for card in cards)
    is_straight = a.get(1) and a.get(10) and a.get(11) and a.get(12) and a.get(13)
    if is_flush and is_straight:
        print("Straight flush")
    elif is_flush:
        print("Flush")
    elif is_straight:
        print("Straight")
    else:
        print("High card")
'''


cards=list(map(int, input().split()))


a={}


for card in cards: #看牌出現幾次
    rank=(card-1)%13+1
    if rank in a:
        a[rank]+=1

    else:
        a[rank]=1

cards.sort()
is_flush=all(card in range(cards[0]%13, cards[0]%13 + 13) for card in cards)
is_straight=(cards[0]%13+5)==(cards[1]%13+4)==(cards[2]%13+3)==(cards[3]%13+2)==(cards[4]%13+1)
is_straight_flush = is_flush and is_straight

if is_straight_flush:
    print("Straight flush")
elif len(a) == 2:
    for count in a.values():
        if count == 4:
            print("Four of a kind")
        elif count == 3:
            print("Full house")
elif len(a) == 3:
    for count in a.values():
        if count == 3:
            print("Three of a kind")
        elif count == 2:
            print("Two pair")
elif len(a) == 4:
    print("One pair")
else:
    if is_flush:
        print("Flush")
    elif is_straight:
        print("Straight")
    else:
        print("High card")