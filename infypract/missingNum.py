cases=int(input())
op=''
while cases>0:
    intsCount=int(input())
    x = [int(x) for x in input().split(" ")]
    # for i in range(len(x)):
    #     if(x[i+1]!=x[i]+1 and i+1<=len(x)):
    #         op+=str(x[i+1])
    # print(op)
    sum_total=int(intsCount*(intsCount+1)/2)
    total=sum(x)
    print(sum_total-total)
    cases-=1