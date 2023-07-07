if __name__ == '__main__':
    # 讀取使用者輸入的電阻值和電阻數量
    resistance = int(input("Please enter the resistance (1-100): "))
    n = int(input("Please enter n (1-100): "))

    # 計算並輸出等效電阻
    if n == 1:
        print(f"Ans: {resistance*2}")
    elif n == 2:
        print(f"Ans: {resistance}")
    else:
        print(f"Ans: {resistance/2*(n-1)+resistance/2}")