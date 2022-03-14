t=int(input())
while(t>0):
    x,y=input().split(" ")
    a=int(x)%2
    b=int(y)%2
    xdividableOrNot= True if(a==0) else False
    ydividableOrNot=True if(b==0) else False
    if(xdividableOrNot==True and ydividableOrNot==True and (x+y)>0):
        print("YES")
    else:
        print("NO")

    # petrolPriceAfterK=int(x)*int(1)
    # dieselPriceAfterK=int(y)*int(2)
    # if(petrolPriceAfterK < dieselPriceAfterK):
    #     print("PETROL")
    # elif(dieselPriceAfterK < petrolPriceAfterK):
    #     print("DIESEL")
    # else:
    #     print("SAME PRICE")
        
    t-=1