
def print_cuboid(l, w, h):
    if l < 4 or w < 4 or h < 4:
        print("錯誤：長、寬和高必須至少為 4")
        return

    colors = ["\033[34m", "\033[42m", "\033[43m"]

    print("#"*(2*l+2))  # 印出立方體的上面
    for i in range(h):
        print("#", end="")  # 印出左邊的邊緣
        for j in range(w):  # 印出立方體內部
            for k in range(l):
                color = colors[(i+j+k) % 3]
                print(color + " " + "\033[0m", end="")
            print(" ", end="")

        print("#")  # 印出右邊的邊緣和外部的空格
    print("#"*(2*l+2))  # 印出立方體的下面


l = int(input("Length: "))
w = int(input("Width: "))
h = int(input("Height: "))
n = int(input("Amount: "))
for i in range(n):
    print_cuboid(l, w, h)
    if i < n-1:
        print(" "*2*l)