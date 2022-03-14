# collections : counter ,namedtuple, orderedDict, defaultdict, deque 
from collections import Counter 
a="aaaabbbbccc"
my_counter=Counter(a)
print(my_counter)
for i,j in my_counter.items():
    print(i,j)

'''=>>
Counter({'a': 4, 'b': 4, 'c': 3})
a 4
b 4
c 3
'''