def h(n, source, target, spare):
    if n == 1:
        print("Move disk 1 from {} to {}".format(source, target))
    else:
        h(n - 1, source, spare, target)
        print("Move disk {} from {} to {}".format(n, source, target))
        h(n - 1, spare, target, source)


n = int(input("數量: "))

h(n, '1', '2', '3')