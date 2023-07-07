import math

a= 0
binary = [0] * 64
# hex = [0] * 16
operation = 0

a= int(input("Please enter a 64-bit integer: "))

# decimalToHex(hex, input)

while True:
    print("--> Decimal:", input)
    print("--> Hex:", format(input, '016X'))
    print("--> Binary:", end=" ")
    for i in range(64):
        print(binary[i], end="")
        if (i + 1) % 8 == 0:
            print(" ", end="")
    print()
    operation = int(input("Operation: "))
    while operation > 7 or operation < 1:
        print("Please enter again")
        operation = int(input("Operation: "))


def decimalToBinary(a):
    binary = [0] * 64
    for i in range(63, -1, -1):
        binary[i] = a% 2
        a//= 2
    return binary

def binaryToDecimal(binary):
    ans = 0
    for i in range(63, -1, -1):
        ans += binary[i] * int(math.pow(2, 63 - i))
    return ans

def decimalToHex(input):
    hex_map = "0123456789abcdef"
    hex_str = ""
    while a!= 0:
        hex_str = hex_map[a% 16] + hex_str
        a//= 16
    return hex_str

decimalToBinary(binary, input)

def main():
    binary = [0] * 64
    a= 0
    while True:
        print("Please select an operation:")
        print("1. Swap two bits")
        print("2. Swap two bytes")
        print("3. Invert a bit")
        print("4. Invert a byte")
        print("5. Set a bit")
        print("6. Set a byte")
        print("7. Exit")
        operation = int(input())

        if operation == 1:
            a, b = 0, 0
            while True:
                a, b = map(int, input("Enter two bit indices (0-63): ").split())
                if a > 63 or a < 0 or b > 63 or b < 0:
                    print("Please enter valid indices")
                    continue
                break
            binary[63 - a], binary[63 - b] = binary[63 - b], binary[63 - a]
            a= binaryToDecimal(binary)

        elif operation == 2:
            a, b = 0, 0
            while True:
                a, b = map(int, input("Enter two byte indices (0-15): ").split())
                if a > 15 or a < 0 or b > 15 or b < 0:
                    print("Please enter valid indices")
                    continue
                break
            a *= 8
            b *= 8
            for i in range(7, -1, -1):
                binary[63 - a], binary[63 - b] = binary[63 - b], binary[63 - a]
                a += 1
                b += 1
            a= binaryToDecimal(binary)

        elif operation == 3:
            a = 0
            while True:
                a = int(input("Enter a bit index to invert (0-63): "))
                if a > 63 or a < 0:
                    print("Please enter a valid index")
                    continue
                break
            binary[63 - a] = 1 - binary[63 - a]
            a= binaryToDecimal(binary)

        elif operation == 4:
            a = 0
            while True:
                a = int(input("Enter a byte index to invert (0-15): "))
                if a > 15 or a < 0:
                    print("Please enter a valid index")
                continue
            break
            a *= 8
            for i in range(7, -1, -1):
                binary[63 - a] = 1 - binary[63 - a]
                a += 1
            a= binaryToDecimal(binary)
        elif operation == 5:
            a = 0
            while True:
                a = int(input("Enter a bit index to set (0-63): "))
                if a > 63 or a < 0:
                    print("Please enter a valid index")
                    continue
                break
            binary[63 - a] = 1
            a= binaryToDecimal(binary)

        elif operation == 6:
            a = 0
            while True:
                a = int(input("Enter a byte index to set (0-15): "))
                if a > 15 or a < 0:
                    print("Please enter a valid index")
                continue
            break
            a *= 8
            for i in range(7, -1, -1):
                binary[63 - a] = 1
                a += 1
                a= binaryToDecimal(binary)

        elif operation == 7:
            break

        else:
            print("Invalid operation")

    print("Binary: " + "".join(str(bit) for bit in binary))
    print("Decimal: " + str(input))
    print("Hexadecimal: " + decimalToHex(input))
