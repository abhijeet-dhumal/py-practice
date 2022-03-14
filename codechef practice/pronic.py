import math 
from itertools import combinations
instr=input()
temp=set()
output=[]
temp1=set()

for i in range(1,len(instr)):
    combs=combinations(instr,i) 
    for j in combs:
        k=int("".join(j))
        temp1.add(k)
# print(sorted(temp1))
for i in range(0,len(instr)):
    for j in range(i,len(instr)):
        k=int(instr[i:j+1])
        temp.add(k)
temp1=sorted(list(temp1))
# print(temp)
for num in temp1:
    for val in range(0,int(math.sqrt(num))+1):
        if val*(val+1)==num:
            output.append(num)
            break 
print(output)