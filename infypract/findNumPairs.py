def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)

# print(factorial(4))
cases=int(input())
while cases>0:
    ints=int(input())
    binary=list(input())
    c=binary.count('1')
    print(int(factorial(c)/(factorial(2)*factorial(c-2))))
    cases-=1