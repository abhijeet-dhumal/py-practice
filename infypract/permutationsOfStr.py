
from itertools import permutations
cases=int(input())
lis=[]
while cases>0:
    stri=input()
    for i in permutations(stri):
        lis.append(''.join(i))
    print(' '.join(lis))
    print(len(lis))
    cases-=1

