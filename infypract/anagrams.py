cases=int(input())
while cases>0:
    s1=input()
    s2=input()
    s1_count=[0]*26
    s2_count=[0]*26

    for i in s1:
        s1_count[(ord(i)-97)] += 1
    for i in s2:
        s2_count[(ord(i)-97)] += 1
    # print(s1_count)
    # print(s2_count)
    count=0
    for i in range(len(s1_count)):
        if s1_count[i]!=s2_count[i]:
            count=count+1
    

    print(count)


    cases-=1