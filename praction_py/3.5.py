
def m():
    A = input("Please enter the first number (A) in binary: ")
    B = input("Please enter the second number (B) in binary: ")


    A_dec = int(A, 2)
    B_dec = int(B, 2)

    result_dec = A_dec * B_dec

    result_bin = bin(result_dec)[2:]
    result_dec = int(result_bin, 2)


    print(f"A = {A} (2) = {A_dec} (10)")
    print(f"B = {B} (2) = {B_dec} (10)")
    print(f"A x B = {result_bin} (2) = {result_dec} (10)")

m()
