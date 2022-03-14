stri=input()
listchar=[]
for i in range(len(stri)):
    if ascii(stri[i])<ascii(stri[i+1]):
        listchar.append(stri[i])
        listchar.append(stri[i+1])
    else:
        listchar.append(stri[i+1])
        break
# listchars=list(set(listchar))
lst=[]
for i in listchar:
    if i not in lst:
        lst.append(i)
if len(lst)>3:
    print(''.join(lst))
else:
    print(-1)
