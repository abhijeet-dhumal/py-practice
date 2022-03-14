def pall(s):
    if s==s[::-1]:
        return True 
    else:
        return False
v='aeiouAEIOU'
st=input().split()
put=[]
for i in range(len(st)):
    
    if pall(st[i])==False:
        out=[]
        add=[]
        for j in range(len(st[i])):
            if st[i][j] in v and j%2==0:
                add.append(st[i][j])
            else:
                out.append(st[i][j]) 
        put.append("".join(out)+"".join(add)) 

    if pall(st[i]):
        out=[]
        add=[]
        for j in range(len(st[i])):
            if st[i][j] in v:
                add.append(st[i][j])
            else:
                out.append(st[i][j]) 
        add.sort()
        put.append("".join(add)+"".join(out))
output=[]
for i in range(len(put)):
    if i%2!=0:
        output.append(put[i])
for j in range(len(put)):
    if j%2==0:
        output.append(put[j])
print(*output,sep=",")