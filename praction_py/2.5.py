def cuboids(length, width, height, h, amount):
    check = 0

    # A
    for i in range(width):
        for a in range(amount):
            for j in range(i, width - 1):
                print(" ", end="")
            if i == 0 or i == width - 1:
                for j in range(length):
                    print("#", end="")
                if i == 0:
                    print(" ", end="")
            else:
                for j in range(length):
                    if j == 0 or j == length - 1:
                        print("#", end="")
                    else:
                        print("\033[41m \033[0m", end="")
            for j in range(i):
                if j == i - 1 and i < height:
                    print("# ", end="")
                elif i >= height:
                    check = 1
                    break
                else:
                    print("\033[45m \033[0m", end="")
            if check == 1:
                for j in range(width + 1):
                    if j < width:
                        if j == height - 2:
                            print("#", end="")
                        elif j > height - 2 and j <= i:
                            print(" ", end="")
                        elif j <= i:
                            print("\033[45m \033[0m", end="")
            print()

    # B
    for i in range(height):
        for a in range(amount):
            if i == height - 1:
                for j in range(length + width - 1):
                    if j < length:
                        print("#", end="")
                    else:
                        print(" ", end="")
                print(" ", end="")
            elif i != 0:
                for j in range(length):
                    if j == 0 or j == length - 1:
                        print("#", end="")
                    else:
                        print("\033[43m \033[0m", end="")
                for j in range(width + 1):
                    if h - width <= 0:
                        if j < width:
                            if j == height - i - 2:
                                print("#", end="")
                            elif j > height - i - 2:
                                print(" ", end="")
                            else:
                                print("\033[45m \033[0m", end="")
                    else:
                        if j == width - 2:
                            print("# ", end="")
                        elif j < width - 2:
                            print("\033[45m \033[0m", end="")
            print()

        h -= 1
        if i != 0:
            print()


if __name__ == "__main__":
    length = 0
    width = 0
    height = 0
    amount = 0

    print("Welcome to Cuboid Super Infinity Exporter!")
    print("Please enter Length, Width and Height of cuboid")
    length = int(input("Length: "))
    width = int(input("Width: "))
    height = int(input("Height: "))
    print("How many cuboids do you want to generate?")
    amount = int(input("Amount: "))

    range = length * 2 + width - 1
    r = (range + 1) * amount - 1
    a = 0

    if r >= 80:
        a = 0
    else:
        a = amount

    if length < 4 or width < 4 or height < 4:
        print("Invalid input")
        exit()
    if range > 80:
        print("Invalid input")