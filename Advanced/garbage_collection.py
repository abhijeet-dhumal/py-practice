'''
Garbage collection :

gc module 

1. gc.isenabled() 
2. gc.disable()
3. gc.enable()

__init__(self): --> constructor
__del__(self): --> destructor
    just before destroying an object, 
    GC calls destructor to perform cleanup activities.
'''

import gc 
# print(gc.isenabled())
'''=>>
True
'''
# gc.disable()
# print(gc.isenabled())
'''=>>
False
'''
# gc.enable()
# print(gc.isenabled())
'''=>>
True
'''

