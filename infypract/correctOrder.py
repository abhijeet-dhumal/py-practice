cases=int(input())
while(cases>0):
    size=int(input())
    lis=[int(x) for x in input().split(" ")]
    nlis=lis.copy()
    nlis.sort()
    lis1=[]
    print(lis,nlis)
    for i in lis:
        lis1.append(nlis.index(i))
    print(lis1)
    cases-=1
    