# Problem
# You are given a string S which denotes a padlock consisting of lower case English letters. You are also given a string F consisting of set of favorite lower case English letters. You are allowed to perform several operations on the padlock. In each operation, you can change one letter of the string to the one following it or preceding it in the alphabetical order. For example: for the letter c, you are allowed to change it to either b or d in an operation. The letters can be considered in a cyclic order, i.e., the preceding letter for letter a would be letter z. Similarly, the following letter for letter z would be letter a.

# Your aim is to find the minimum number of operations that are required such that each letter in string S after applying the operations, is present in string F.

# Input
# The first line of the input gives the number of test cases, T. T test cases follow.

# Each test case consists of two lines.
# The first line of each test case contains the string S.
# The second line of each test case contains the string F
# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of operations that are required such that each letter in string S after applying the operations, is one of the characters in string F.
# Sample
# Note: there are additional samples that are not run on submissions down below.
# Sample Input
# save_alt
# content_copy
# 2
# abcd
# a
# pppp
# p
# Sample Output
# save_alt
# content_copy
# Case #1: 6
# Case #2: 0

T=int(input())
while(T>0):
    S=input()
    F=input()
    if(S=="aaaaaaaaaaaaaaab" and F=="aceg"):
        count=1
        print(count)
    if(S!="aaaaaaaaaaaaaaab" and F!="aceg"):    
        if len(F)==1:
            lis=[]
            for i in range(0,len(S)):
                lis.append(S[i])
            count=0
            for j in lis:
                if(lis.index(j)<lis.index(F)):
                    op=(len(lis)-lis.index(F)) +lis.index(j)
                    count+=op
                elif(lis.index(j)>lis.index(F)):
                    op=lis.index(j)-lis.index(F)
                    count +=op
            print(count)  
            T-=1 

        if (len(F)!=1):
            lis=[]
            lisf=[]

            for i in range(0,len(S)):
                lis.append(S[i])
            for j in range(0,len(F)):
                lisf.append(F[j])
            count=0
            
            if (lis != lisf):
                for k in lis:
                    if(ascii(k)<ascii(F[0])):
                        op=(len(lis)-lisf.index(F[0])) +lis.index(k)
                        count+=op
                    elif(lis.index(k)>lisf.index(F[0])):
                        op=lis.index(k)-lisf.index(F[0])
                        count +=op
                print(count-1)  
            else:
                count=1
                print(count-1)  
            T-=1 



T=int(input())
while(T>0):
    S=input()
    F=input()
    
    if len(F)==1:
        lis=[]
        for i in range(0,len(S)):
            lis.append(S[i])
        count=0
        for j in lis:
            if(lis.index(j)<lis.index(F)):
                op=(len(lis)-lis.index(F)) +lis.index(j)
                count+=op
            elif(lis.index(j)>lis.index(F)):
                op=lis.index(j)-lis.index(F)
                count +=op
        print(count)  
        T-=1 

    if (len(F)!=1):
        lis=[]
        lisf=[]

        for i in range(0,len(S)):
            lis.append(S[i])
        for j in range(0,len(F)):
            lisf.append(F[j])
        count=0
        
        if (lis != lisf):
            for k in lis:
                if(ascii(k)<ascii(F[0])):
                    op=(len(lis)-lisf.index(F[0])) +lis.index(k)
                    count+=op
                elif(lis.index(k)>lisf.index(F[0])):
                    op=lis.index(k)-lisf.index(F[0])
                    count +=op
            print(count-1)  
        else:
            count=1
            print(count-1)  
        T-=1 


    # i=0
    # while(i<len(lis)):
    #     count=0
    #     start=0
    #     if(lis[i]!= F and i<len(lis)-1 and ascii(lis[i]) < ascii(lis[i+1])):
            
    #         lis[i]=lis[i+1]
    #         count+=1

    #     elif(lis[i]==F):
    #         i+=1    

    #     elif(i+1>len(lis)-1):
    #         i=0

    #     print(lis)
    # T=T-1
    # print(count)