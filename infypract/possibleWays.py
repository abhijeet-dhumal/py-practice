def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)

cases=int(input())
op=''
while cases>0:
    m,n=input().split(" ")
    m,n=int(m),int(n)
    print(int(factorial(m+n)/(factorial(m)*factorial(n))))
    cases-=1