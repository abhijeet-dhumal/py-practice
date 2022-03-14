from itertools import permutations,combinations, product
from math import sqrt
def prime(n):
    prime_flag = 0
  
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

s=input()
l=[]
for i in s:
    o=ord(i)
    l.append(str(o))

lst=[p for p in product(l, repeat=3)]
# print(lst)
out=[]
for i in lst:
    if prime(int("".join(i))):
        out.append(i)
put=[]
for i in out:
    st=''
    for j in i:
        st+=chr(int(j))
    put.append(st)
put.sort()
if len(put)!=0:    
    print(*put,sep=',')
else:
    print(-1)
