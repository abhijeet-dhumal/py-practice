def countPrint(countList):
    for j in countList:
        if int(j)>(size/2):
              return j
    return -1

cases=int(input())
while(cases>0):
    size=int(input())
    countList=[0]*(11)
    x=[x for x in input().split(" ")]
    count=0
    for i in x:
        countList[(int(i))]=countList[(int(i))]+1
    print(countList)
    print(countPrint(countList))
    
          
    cases-=1