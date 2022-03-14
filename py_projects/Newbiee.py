# cook your dish here
p,c= map(int,input().split())
contributors=[]
dicti=dict()
for i in range(p):
    name,o=map(str,input().split())  
    contributors.append(name)
    l=[]
    o=int(o)
    d=dict()
    dicti[name]=d
    for i in range(o):
        inp=[i for i in input().split()]
        d[inp[0]]=int(inp[1])
        # l.append(d)
print(dicti)

def check(n,p):
    for key,value in dicti.items():
        # print(key,value)
        pass
        for i,j in value.items():
            a,b=i,j
            if i==n and j>=p:
                return key
'''
n-no.of days to complete project
s=score awareded for project complettion
d= the “best before” day for the project
r=the number of roles in the project

3
WebServer
Bob Anna
Logging
Anna
WebChat
Maria Bob

'''
projects=[]
dictio=dict()
for i in range(c):
    name_p,n,s,d,r=map(str,input().split()) 
    projects.append(name_p)
    n=int(n)
    s=int(s)
    d=int(d)
    r=int(r)
    lst=[]
    di=dict()
    dictio[name_p]=di
    for i in range(r):
        inp=[i for i in input().split()]
        di[inp[0]]=int(inp[1])
        
print(dictio)
print(len(dictio))
for key,value in dictio.items():
    print(key)
    p=[]
    for i,j in value.items():
        p.append(check(i,j))
    print(*p)    
    if len(p)==len(value):
        for i,j in value.items():
            for m,n in dicti.items():
                for l,k in n.items():
                    if j==k:
                        n[l]=k+1
                        print(j,k)

print(dicti)
        
    


