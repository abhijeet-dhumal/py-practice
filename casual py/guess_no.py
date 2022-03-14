while(True):
    i = 5
    while i > 0:
        n=int(input("Enter a number : "))
        if n<100:
            print("Entered number is too less,.\nTry again!!!")
        elif n>100:
            print("Entered number is greater,.\nTry again!!!")
        elif n==100:
            print("Congratulations!!!,. \nYou entered correct number...")
            break
        i=i-1
        print("Number of guesses remained are :", i)
        if i==0:
            print("--------------------------------------------")
            print("Game Over!!!")
    break