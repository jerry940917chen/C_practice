import numpy as np

x1 = 15
y1 = 15

# 初始化画布和颜色板
#canvas = np.zeros((x1, y1))
canvas = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
          [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
          [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
          [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
          [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]


color = np.zeros((x1, y1), dtype=int)


print("   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
for i in range(x1):
    print(f"{i:2d}", end=" ")
    for j in range(y1):
        if canvas[i][j] == 1:
            print("  ", end="")
        elif color[i][j] == 0:
            print("\033[47;37m  \033[0m", end="")
        elif color[i][j] == 1:
            print("\033[41;37m  \033[0m", end="")
        elif color[i][j] == 2:
            print("\033[43;37m  \033[0m", end="")
        elif color[i][j] == 3:
            print("\033[42;37m  \033[0m", end="")
        elif color[i][j] == 4:
            print("\033[44;37m  \033[0m", end="")
    print()

while True:
    while True:
        x, y = map(int,input("x,y: ").split(','))
        if x > x1 - 1 or x < 0 or y > y1 - 1 or y < 0:
            print("範圍錯誤")
            continue
        break
    while True:
        color_1 = int(input("0-4: "))
        if color_1 > 4 or color_1 < 0:
            print("範圍錯誤")
            continue
        break
    color[x][y] = color_1
    # 更新后的表格
    print("   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
    for i in range(x1):
        print(f"{i:2d}", end=" ")
        for j in range(y1):
            if canvas[i][j] == 1:
                print("  ", end="")
            elif color[i][j] == 0:
                print("\033[47;37m  \033[0m", end="")
            elif color[i][j] == 1:
                print("\033[41;37m  \033[0m", end="")
            elif color[i][j] == 2:
                print("\033[43;37m  \033[0m", end="")
            elif color[i][j] == 3:
                print("\033[42;37m  \033[0m", end="")
            elif color[i][j] == 4:
                print("\033[44;37m  \033[0m", end="")
        print()
def draw(board, x, y, color):
    x1 = len(board)
    y1 = len(board[0])
    
    if board[x][y] == 1:
        return
    if x == 0 and y == 0:
        board[x][y] = color
        if board[x + 1][y] != color:
            draw(board, x + 1, y, color)
        if board[x][y + 1] != color:
            draw(board, x, y + 1, color)
    elif x == 0 and y == y1 - 1:  
        board[x][y] = color
        if board[x + 1][y] != color:
            draw(board, x + 1, y, color)
        if board[x][y - 1] != color:
            draw(board, x, y - 1, color)
    elif x == x1 - 1 and y == 0:  
        board[x][y] = color
        if board[x - 1][y] != color:
            draw(board, x - 1, y, color)
        if board[x][y + 1] != color:
            draw(board, x, y + 1, color)
    elif x == x1 - 1 and y == y1 - 1:
        board[x][y] = color
        if board[x - 1][y] != color:
            draw(board, x - 1, y, color)
        if board[x][y - 1] != color:
            draw(board, x, y - 1, color)
    elif x == 0:  
        board[x][y] = color
        if board[x + 1][y] != color:
            draw(board, x + 1, y, color)
        if board[x][y + 1] != color:
            draw(board, x, y + 1, color)
        if board[x][y - 1] != color:
            draw(board, x, y - 1, color)
    elif x == x1 - 1:  # Bottom row
        board[x][y] = color
        if board[x - 1][y] != color:
            draw(board, x - 1, y, color)
        if board[x][y + 1] != color:
            draw(board, x, y + 1, color)
        if board[x][y - 1] != color:
            draw(board, x, y - 1, color)
    elif y == 0:  # Left column
        board[x][y] = color
        if board[x + 1][y] != color:
            draw(board, x + 1, y, color)
        if board[x - 1][y] != color:
            draw(board, x - 1, y, color)
        if board[x][y + 1] != color:
            draw(board, x, y + 1, color)
    elif y == y1 - 1:  # Right column
        board[x][y] = color
        if board[x + 1][y] != color:
            draw(board, x - 1, y, color)
        if board[x - 1][y] != color:
            draw(board, x - 1, y, color)
        if board[x][y + 1] != color:
            draw(board, x, y + 1, color)
