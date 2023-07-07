number1=int(input("Please enter the first number"))
number2=int(input("Please enter the second number"))
a=int(number1)
b=int(number2)
c=a-b
if c>=0:
    c=str(a-b)
    number1=str(number1)
    number2=str(number2)
    print("  "+number1+'\n'+"-)"+number2+'\n'+"------"+'\n'+"  "+c)
else:
    c=str(a-b)
    number1=str(number1)
    number2=str(number2)
    print("  "+number1+'\n'+"-)"+number2+'\n'+"------"+'\n'+" "+c)
