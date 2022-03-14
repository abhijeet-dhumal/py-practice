t=int(input())
while(t>0):
    x,y,a,b,k=input().split(" ")
    petrolPriceAfterK=int(x)+int(k)*int(a)
    dieselPriceAfterK=int(y)+int(k)*int(b)
    if(petrolPriceAfterK < dieselPriceAfterK):
        print("PETROL")
    elif(dieselPriceAfterK < petrolPriceAfterK):
        print("DIESEL")
    else:
        print("SAME PRICE")
        
    t-=1