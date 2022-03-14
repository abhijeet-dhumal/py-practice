from sys import stdin 

def checkPalindromic(x):
    if x==x[ : :-1]:
        True
    else:
        False

t=int(input())
while(t>0):
    n=int(input())
    x = [int(x) for x in input().split(" ")]
    s=[]
    for i in range(0,len(x)):
        g= chr(i+97)*x[i]
        s.append(g)
    print(s)
    if(checkPalindromic(s)):
        print(0)
    else:
        print(1)
    t-=1

