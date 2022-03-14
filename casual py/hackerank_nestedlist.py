if __name__ == '__main__':
    marksheet=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name,float(score)]) 
    # 1
    marksheet.sort(key=lambda x:x[1])    
    a=marksheet[1][1]
    n=len(marksheet)
    lst1=[]    
    for i in marksheet:
        if i[1]==marksheet[1][1]:
            lst1.append(i[0])
    lst1.sort()
    for k in lst1:
        print(k)
    
    # 2
    second_highest = sorted(list(set([scores for name, scores in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
