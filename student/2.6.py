n = int(input("請輸入一個正整數："))

prime_numbers = []

# 從2開始遍歷到n，判斷每個數字是否為質數
for num in range(2, n+1):
    # 假設該數字是質數
    is_prime = True
    # 從2到num-1遍歷每個數字，判斷是否能整除num
    for i in range(2, num):
        if num % i == 0:
            # 如果num能被i整除，則num不是質數，標記為False
            is_prime = False
            break
    # 如果num是質數，則將其添加到prime_numbers列表中
    if is_prime:
        prime_numbers.append(num)

print("在", n, "之前的所有質數為：", prime_numbers)