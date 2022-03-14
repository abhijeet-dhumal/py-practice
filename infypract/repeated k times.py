inp_length=int(input())
inp_lst=[int(x) for x in input().split(" ")]
lst=[0]*100001
for i in inp_lst:
    lst[i]+=1
inp=int(input())
for i in lst:
    if inp_lst.count(i)==inp:
        lst.append(i)
print(min(lst))