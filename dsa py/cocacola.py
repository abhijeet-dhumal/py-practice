number=int(input())
lst_tin=[1,3,5,7,10]
minnum=number%10
if number>0:
    if minnum==0:
        print(int(number/10))
    elif minnum in lst_tin:
        print(int(number/10)+1)
    elif minnum not in lst_tin:
        num=[]
        for i in lst_tin:
            if i<minnum:
                num.append(i)
        print(int(number/10)+len(num))
    else :
        print(int(minnum)+int(number/10))
else:
    print(0)