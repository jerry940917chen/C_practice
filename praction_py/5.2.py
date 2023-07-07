def mymemcmp(s1, s2):
    #檢查長度
    if len(s1) != len(s2):
        return False
    #檢查每個單字
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True
s1 = b"Hello, world!"
s2 = b"Hello, Python!"
if mymemcmp(s1, s2):
    print("The two strings are equal.")
else:
    print("The two strings are not equal.")