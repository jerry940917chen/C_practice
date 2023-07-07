n, eng_limit, clean_limit, clown_limit = map(int, input().split())

# 將每個應徵者的實力按照三種工作分開存放
engineer = [0] * n
cleaner = [0] * n
clown = [0] * n

for i in range(n):
    x, y, z = map(int, input().split())
    engineer[i] = x
    cleaner[i] = y
    clown[i] = z
#OK
# 建立三維的dp table，第一維是應徵者的序號，第二維是工程師的名額數，第三維是清潔工的名額數
dp = [[[0] * (clean_limit+1) for _ in range(eng_limit+1)] for _ in range(n+1)]

# 從第1位應徵者開始填表
for i in range(1, n+1):
    # 依次枚舉可用的工程師和清潔工名額數，計算最大實力總和
    for j in range(eng_limit+1):
        for k in range(clean_limit+1):
            # 計算不錄用第i位應徵者時的最大實力總和
            nohire = dp[i-1][j][k]
            # 計算將第i位應徵者錄用為工程師時的最大實力總和
            eng = engineer[i-1]
            if j > 0:
                eng += dp[i-1][j-1][k]
            # 計算將第i位應徵者錄用為清潔工時的最大實力總和
            clean = cleaner[i-1]
            if k > 0:
                clean += dp[i-1][j][k-1]
            # 計算將第i位應徵者錄用為工程師和清潔工時的最大實力總和
            eng_clean = engineer[i-1] + cleaner[i-1]
            if j > 0 and k > 0:
                eng_clean += dp[i-1][j-1][k-1]
            # 將三種情況的最大值填入dp table
            dp[i][j][k] = max(nohire, eng, clean, eng_clean)

# 最後結果為dp table的最後一個元素
print(dp[n][eng_limit][clean_limit])





"""
sum=0
n = input().split()
n=int(n[0])
for i in range(n):
    p=input().split()
    for j in range(1,n):
        p.sort()
        p.reverse()  
        a=intn[j+1]
        for s in range(1,a):
            sum=int(p[s])+sum
            print(sum)
    b=sum+b
"""