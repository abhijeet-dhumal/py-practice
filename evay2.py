n=int(input())
a,ans=[],[]
for t in range(n):
    a.append(list(map(str,input().split(","))))

m=len(a[0])
l,r,u,d=0,m-1,0,n-1

while(l<=r and u<=d):
    # for i in range(u,d+1):
    #     ans.append(a[i][l])
    # l+=1
    for i in range(u,d+1):
        ans.append(a[0][i])
    l-=1
    # for i in range(l,r+1):
    #     ans.append(a[d][i])
    # d-=1
    for i in range(u,l+1):
        ans.append(a[i][d])
    d-=1
    for i in range(d,u-1,-1):
        ans.append(a[i][r])
    r-=1
    for i in range(r,l-1,-1):
        ans.append(a[u][i])
    u+=1
print(*ans,sep=",")
    