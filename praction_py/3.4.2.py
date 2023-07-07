def hanoi(n, source, target, spare):
    stack = [(n, source, target, spare)]
    while stack:
        n, source, target, spare = stack.pop()
        if n == 1:
            print("Move disk 1 from {} to {}".format(source, target))
        else:
            stack.append((n-1, spare, target, source))
            stack.append((1, source, target, spare))
            stack.append((n-1, source, spare, target))


n = int(input("請輸入盤子數量: "))
hanoi(n, '1', '2', '3')