cases=int(input())
while(cases>0):
    x=input()
    stack=[]
    for i in x:
        if i.isnumeric():
            stack.append(i)
        else:
            num1=int(stack.pop())
            num2=int(stack.pop())
            output=0
            if(i=='*'):
                output=num2*num1
            elif(i=='-'):
                output=num2-num1
            elif(i=='+'):
                output=num2+num1
            elif(i=='/'):
                output=num2/num1
            else:
                print("valid sign")
            stack.append(output)
    print(stack[0])
          
    cases-=1