sum=0
i=0
while True:
    a=int(input(
    "1.Input the course grade."'\n'
    "2.Remove the course grade."'\n'
    "3.GPA report."'\n'
    "4.Target GPA."'\n'
    "5.Exit."'\n'
    "Your Choice (1-5):"
    ))
    if a < 1 or a > 5:
        print("error: wrong input. please enter again")
        continue


    if a == 1:
        b = int(input("b: (1-100): "))
        c = int(input("c (0-4): "))

        if b < 1 or b > 100 or c > 4 or c < 0:
            print("error: wrong input")
            continue

        if b >= 90:
            grade = 4.3
        elif b >= 85:
            grade = 4.0
        elif b >= 80:
            grade = 3.7
        elif b >= 77:
            grade = 3.3
        elif b >= 73:
            grade = 3.0
        elif b >= 70:
            grade = 2.7
        elif b >= 67:
            grade = 2.3
        elif b >= 63:
            grade = 2.0
        elif b >= 60:
            grade = 1.7
        elif b >= 50:
            grade = 1.0
        elif b >= 1:
            grade = 0.0

        i += c
        sum += c * grade

    if a == 2:
        b = int(input("b: (1-100): "))
        c = int(input("c (0-4): "))

        if b < 1 or b > 100 or c > 4 or c < 0:
            print("error: wrong input")
            continue

        if b >= 90:
            grade = 4.3
        elif b >= 85:
            grade = 4.0
        elif b >= 80:
            grade = 3.7
        elif b >= 77:
            grade = 3.3
        elif b >= 73:
            grade = 3.0
        elif b >= 70:
            grade = 2.7
        elif b >= 67:
            grade = 2.3
        elif b >= 63:
            grade = 2.0
        elif b >= 60:
            grade = 1.7
        elif b >= 50:
            grade = 1.0
        elif b >= 1:
            grade = 0.0

        i -= c
        sum -= c * grade
    '''
    if a==1:
        b=int(input("b (0-100)"))
        c=int(input("c (0-4)"))
        sum=b*c+sum
        i+=c
    if a==2:
        d=int(input("b (0-100)"))
        e=int(input("c (0-4)"))
        sum=sum-b*c
        i+=d
    '''
    if a==3:
        print("Total Credits:",format(i))
        print("GPA:",format(float(sum) / i))
        GPA=int(float(sum) / i)
        '''
        z=sum/i
        if 90<=z<=100:
            GPA=sum*4.3/sum
        elif 85<=z<=89:
            GPA=sum*4.0/sum
        elif 80<=z<=84:
            GPA=sum*3.7/sum
        elif 77<=z<=79:
            GPA=sum*3.3/sum            
        elif 73<=z<=76:
            GPA=sum*3.0/sum
        elif 70<=z<=72:
            GPA=sum*2.7/sum
        elif 67<=z<=69:
            GPA=sum*2.3/sum
        elif 63<=z<=66:
            GPA=sum*2.0/sum 
        elif 60<=z<=62:
            GPA=sum*1.7/sum
        elif 50<=z<=59:
            GPA=sum*1.0/sum
        elif 1<=z<=49:
            GPA=sum*0.0/sum                                                             
        print("GPA:",GPA)
        '''
    if a==4:
        f=float(input("Target GPA:"))
        g=int(input("Remaining Credits:"))
        if f > 5 or f < 1 or g < 0:
            print("error: wrong input\n please input again")
            
        if GPA<f:
            #z=(sum+g*100)/(i+g)
            z=(f*(i+g)-sum)/g
            if 90<=z<=100:
                print("需要A+以上")
            elif 85<=z<=89:
                print("需要A以上")
            elif 85<=z<=89:    
                print("需要A-以上")
            elif 77<=z<=79:
                print("需要B+以上")
            elif 73<=z<=76:
                print("需要B以上")
            elif 70<=z<=72:
                print("需要B-以上")
            elif 67<=z<=69:
                print("需要C+以上")
            elif 63<=z<=66:
                print("需要C以上")
            elif 60<=z<=62:
                print("需要C-以上")
            elif 50<=z<=59:
                print("需要D以上")
            elif 1<=z<=49:
                print("需要E以上")          
        else:
            print("GPA已經夠了")
    if a==5:
        break
