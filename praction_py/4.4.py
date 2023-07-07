board = [[-1 for j in range(25)] for i in range(17)]
#先做出25格都是-1的列表，然後再做17層

# Space
for i in range(17):
    for j in range(25):
        board[i][j] = -1

# Yellow
for j in range(1, 5):
    for i in range(j):
        board[j-1][2*i+13-j] = 1
#一行為25個，中間是12，依此類推，2*i+13-j可以算出哪一格

# White
for j in range(13):
    for i in range(13-j):
        board[j+4][2*i+j] = 0

# Green
for j in range(9, 13):
    for i in range(j-8):
        board[j][2*i+12-j] = 2

# Red
for j in range(9, 13):
    for i in range(j-8):
        board[j][2*i+30-j] = 3



def print_board(board):
    for i in range(17):
        for j in range(25):
            if board[i][j] == -1:
                print(" ", end="")
            elif board[i][j] == 0:
                print("*", end="")
            elif board[i][j] == 1:
                print("\033[38;5;220m*\033[m", end="")
            elif board[i][j] == 2:
                print("\033[38;5;28m*\033[m", end="")
            elif board[i][j] == 3:
                print("\033[38;5;124m*\033[m", end="")
        print()
print(print_board(board))