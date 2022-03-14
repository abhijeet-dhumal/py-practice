str=input()
half=len(str)//2
for i in range(half,0,-1):
    pre=str[0:i]
    suffix=str[len(str)-i:len(str)]
    if (pre==suffix):
        print(len(pre))
        break
