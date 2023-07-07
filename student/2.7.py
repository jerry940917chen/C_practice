music = "I'm at a payphone trying to call home\
All of my change I spent on you\
Where have the times gone\
Baby, it's all wrong, where are the plans we made for two?\
Yeah, I, I know it's hard to remember\
The people we used to be\
It's even harder to picture\
That you're not here next to me\
You say it's too late to make it\
But is it too late to try?\
And in our time that you wasted\
All of our bridges burned down\
I've wasted my nights\
You turned out the lights\
Now I'm paralyzed\
Still stuck in that time\
When we called it love\
But even the sun sets in paradise\
I'm at a payphone trying to call home\
All of my change I spent on you\
Where have the times gone\
Baby, it's all wrong, where are the plans we made for two?\
If happy ever after did exist\
I would still be holding you like this\
All those fairy tales are full of shit\
One more fucking love song, I'll be sick"

# 用空白分隔單字，將大寫轉為小寫，並刪除標點符號
words = music.lower().replace(',', '').replace('.', '').replace('?', '').replace('!', '').split()

word_dict = {}
for index, word in enumerate(words):
    if word not in word_dict:
        word_dict[word] = [index]
    else:
        word_dict[word].append(index)
# 計算每個單字出現次數
word_count = {}
for word in word_dict:
    word_count[word] = len(word_dict[word])

print(word_count)