
#Faulty Calculator: perfect calculations except these following: 56+9=77, 45*3=555, 56/6=4
while (True):
    a, b = input("Enter two numbers :\n").split(",")
    a=int(a)
    b=int(b)
    operator=input("Enter operation to be performed :\n")
    if a == 56 and b == 9 and operator=="+":
        print("ans:", "77")
    elif a == 45 and b == 3 and opertor=="*":
        print("ans:", "555")
    elif a == 56 and b == 6 and operator=="/":
        print("division:", "4")
    else:
        if operator== "+":
            print("ans -->", a+b)
        elif operator=="-":
            print("ans -->", a-b)
        elif operator == "*":
            print("ans -->", a*b)
        elif operator == "/":
            print("ans -->", a/b)
    print("--------------------------------------------------------------------------")
