while(True):
    print("How many rows you want print  :")
    n=int(input())
    b=bool(int(input("Enter 1 or 0 :")))
    if b==True:
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()
    else:
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()
