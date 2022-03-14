def m(lst,e):
    i,j=0,e-1
    while i<j:
        if lst[i]!=lst[j]:
            return i,j
        else:
            i+=1 
            j-=1
            

def is_pall(lst,n):
    if lst==lst[::-1]:
        return True 
    else:
        return False
 
e=int(input())
lst=[]
n = len(lst)
for _ in range(e):
    lst.append(int(input()))

if e==1:
    print(0)
elif is_pall(lst,e):
    print(0)
else:
    p=m(lst,e)
    q=[int(i) for i in lst[p[0]:p[1]+1]]
    print(q)
    if len(q)%2==0:
        count=0
        for i in range(len(q)-1):
            b=q.pop(i+1)
            a=q.pop(i)
            
            q.insert(i,a+b)
            
            if not is_pall(q,e):
                count+=1
            else:
                print(count+1)
                break
    else:
        q.pop((len(q)%2+1))
        count=0
        for i in range(len(q)-1):
            b=q.pop(i+1)
            a=q.pop(i)
            
            q.insert(i,a+b)
            
            if not is_pall(q,e):
                count+=1
            else:
                print(count+1)
                break
        
