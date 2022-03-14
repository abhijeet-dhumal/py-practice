cases=int(input())
while cases>0:
    stri1=input()
    stri2=input()
    s1=[x for x in stri1]
    s2=[x for x in stri2]
    stack=[]
    count=0
    string=''
    for i in range(len(s1)):
        if s1[i]=="#":
            count+=1
            s1.insert(i-1,chr(ord(s1[i-1])+count))
            s1.remove(s1[i])
    for i in range(len(s1)):
        if(s1[i]=='#'):
            # string=s1Out[0:i]+s1Out[i+ 1:len(s1Out)]
            s1.remove(s1[i])
            break
    s1Out="".join(s1)
    print(s1Out)
    count1=0
    for j in range(len(s2)):
        if s2[j]=="#":
            count1+=1
            s2.insert(j-1,chr(ord(s2[j-1])+count1))
            s2.remove(s2[j])
    for i in range(len(s2)):
        if(s2[i]=='#'):
            # string=s1Out[0:i]+s1Out[i+ 1:len(s1Out)]
            s2.remove(s2[i])
            break
    s2Out="".join(s2)
    print(s2Out)
    cases-=1