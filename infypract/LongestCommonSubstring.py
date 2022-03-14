cases=int(input())
while cases>0:
    inp=int(input())
    count=0
    while(inp):
        if inp%10==0:
            print(count)
            break
        elif inp==1:
            print(-1)
            break
        elif inp%10!=0:
            inp*=2
            count+=1
    cases-=1