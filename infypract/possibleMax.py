from itertools import permutations
ints=[x for x in input().split(" ")]
comb=[]
maxval=1
for i in permutations(ints):
    comb.append(''.join(i))
for j in range(len(comb)):
    if int(comb[j])>maxval :
        maxval=int(comb[j])
print(maxval)