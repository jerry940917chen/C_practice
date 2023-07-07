Pa, Pb = map(int, input().split())  # 產品甲和乙的售價
Ca, Cb = map(int, input().split())  # 產品甲和乙的售出所需的銷貨成本
Sa, Sb = map(int, input().split())  # 產品甲和乙的目前庫存數量
Ha, Hb = map(int, input().split())  # 產品甲和乙的最低售出量

# 定義最佳解初值
best_profit = 0
best_sold_a = 0
best_sold_b = 0

# 計算產品甲和乙分別能夠售出的數量範圍
max_sold_a = Sa - Ha
max_sold_b = Sb - Hb

# 枚舉所有可能的銷售策略
for sold_a in range(Ha, max_sold_a + 1):
    for sold_b in range(Hb, max_sold_b + 1):
        # 計算淨獲利
        profit = sold_a * (Pa - Ca) + sold_b * (Pb - Cb)

        # 更新最佳解
        if profit > best_profit:
            best_profit = profit
            best_sold_a = sold_a
            best_sold_b = sold_b

# 輸出結果
print(best_profit)
print(best_sold_a, best_sold_b)