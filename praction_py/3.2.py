import math

def get_stddev():
    numbers = []
    while True:
        num = input("請輸入一個數字 (輸入 'done' 結束輸入): ")
        if num == "done":
            break
        try:
            num = float(num)
            numbers.append(num)
        except:
            print("輸入無效，請輸入一個數字或 'done' 結束輸入")

    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum([(x - mean) ** 2 for x in numbers]) / n
    #sum([(x - mean) ** 2 for x in numbers]) / n：使用列表推導式計算數字列表的變
    stddev = math.sqrt(variance)
    return stddev

print(get_stddev())