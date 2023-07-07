n = int(input())

# 生成單向通道
edges = []
for i in range(2, n+1):
    for j in range(1, i):
        edges.append((j, i))


# 輸出結果
print(len(edges))
for e in edges:
    print(e[0], e[1])
print(n,"35")
#for r in routes:
    #for i in range(len(r)-1):
     #   print(r[i], r[i+1])