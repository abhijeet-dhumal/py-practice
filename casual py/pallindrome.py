print(*['Not Palindrome' if len([rec for rec in {i for i in 'aaabbbccc'} if 'aaabbbccc'.count(rec)%2!=0])>1 else 'Palindrome'])
from itertools import combinations
print(["Pallindrome" if ([i for i in combinations("aaabbbccc",9)]==[i for i in combinations("aaabbbccc",9)][::-1]) else 'Not pallindrome'])
