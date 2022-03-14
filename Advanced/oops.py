'''
class --> blueprint, template which consists of code methods to perform while called. 
object --> physical instance  of class which calls class to perform methods associated.
constructor --> The name should should be always '__init__'. whenever we are creating an object 
                counstructor will be execured automatically no need to call it explicitly. 
                The main objective of constructor is to initialize the instance variable.
                For every object constructor will execute only once. 
                atleast one argument self .
                python will provide default constructor incase constructor is not specified.
self --> self is an implicit variable which is always provided by pvm.
        self is always pointing to current object .
        For every constructor and instance method the first argument should be self.
        within the class self can be usedto declare instance variables and to access instance variables .

'''

# class Doc:
#     '''This is docstring !!!'''

# print(Doc.__doc__) 
'''
=>>C:\py_practice\Advanced>py oops.py
This is docstring !!!
'''

# print(help(Doc))
'''
Help on class Doc in module __main__:

class Doc(builtins.object)
 |  This is docstring !!!
 |  
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

None
'''
# class Employee:
#     '''doc string(description)'''
#     def __init__(self,eno,ename,esalary,eaddress):
#         ''' self is a reference variable which is always pointing to current object '''
#         '''instance variables'''
#         self.eno=eno
#         self.ename=ename
#         self.esalary=esalary
#         self.eaddress=eaddress

#     def info(self):
#         print('*'*20)
#         print(f"Employee number: {self.eno}")
#         print(f"Employee name: {self.ename}")
#         print(f"Employee salary: {self.esalary}")
#         print(f"Employee address: {self.eaddress}")
#         print('*'*20)

# e1=Employee(101,"Kunal Kushwaha",30000,"Pune")  
'''object syntax ,reference variable e1 to which object is assigned'''

# print(e1.eno)
'''=>> 101'''
# e1.info()  
'''=>>
********************
Employee number: 101
Employee name: Kunal Kushwaha
Employee salary: 30000
Employee address: Pune
********************
'''      
# e2=Employee(102,"Abhijeet Dhumal",30000,"Delhi") 

# print(e2) 
'''=>> 
<__main__.Employee object at 0x000002635E403FD0>
'''
# print(e2.info()) 
'''=>>
********************
Employee number: 102
Employee name: Abhijeet Dhumal
Employee salary: 30000
Employee address: Delhi
********************
'''



# class Test:
#     def __init__(self):
#         print("Constructor execution...")

# t=Test()
'''=>>
Constructor execution...
'''

'''______________________________________________________________________________________________________'''


# class Test:
#     def __init__(self):
#         print("No-arg")
    
#     def __init__(self,x):
#         print("One-arg")
    

# t=Test()
# t2=Test(10)
'''=>>
__init__() missing 1 required positional argument: 'x'
'''
'''In python constructor or method overloading concept not applicable, 
it will override first init constructor with 0 args and then will execute second init with one argument'''

# t2=Test(10)
'''=>> One-arg'''


'''______________________________________________________________________________________________________'''

