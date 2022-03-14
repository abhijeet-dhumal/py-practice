'''
In python class 3 types of variables :
1) Instance variables / object level variables : 
            value of varibles varries from object to object ,such variabes are called instanve variables.
            variables which are initialzed using self inside constructor.
2) Static variables / class level variables :
            for all objects only one copy will be created and this copy is shared to all variables of that class
            declared within class but outside of any methods and constructor.
3) Local variables / method variable :
            variables which are declared in methods for only local purpose

In python class 3 types of methods :
1) Instance methods / object related methods :
            methods in which we are using objects related instance variables
2) Static methods/utility methods : not object related at all.
3) Class methods : not object replated ,only class related


instance variables:
    object level variables 
    by using self(within the class) or by using object referenece (outside of class)

static variables :
    class level variables
    directly by using cls variable 
    by using classname from outside of the class 

Local variables:
    Method level variables
    we should not use self,cls,classname

    From the class we can access global variables directly 
    within the method of a class we can declare global variables by using global keyword.

'''

# class Student:
#     cname="Durgasoft" #static variable
#     def __init__(self,x,y):
#         count=0 #local / method variable
#         self.name=x # instance variable
#         self.id=y # instance variable

#     def display(self): # Instance methods / object related methods 
#         print(f"Hello,Myself {self.name} and my id is {self.id}")

#     @classmethod #by using this decorator ,this method will be treated as class level method
#     def getCollegeName(cls): # class methods : cls is always required as it represents class name
#         print(f"College name : '{cls.cname}' ")

#     @staticmethod 
#     def findavg(x,y): #static method
#         print(f"Average is : {(x+y)//2}")


# s1=Student("Durga",101)
# s2=Student("Shiva",102)
# Student.getCollegeName() 
'''=>> College name : 'Durgasoft' '''
# s1.findavg(2,3) 
'''=>> Average is : 2'''
# Student.findavg(2,3) 
'''=>> Average is : 2'''



'''
Instance variables :
    value of variable varies with object to object
    for every object a separate copy will be created 

where we have to declare instance variables:
1. Inside constructr by using self 
2. Inside instance method by using self 
3. From outside of the class by using object reference
'''

# class Student:
#     cname="Durgasoft" 
#     def __init__(self,x,y):
#         self.name=x 
#         self.rollno=y

#     def info(self): # Instance methods / object related methods 
#         self.marks=50
    
# s1=Student("Durga",101)
# s1.info()
# s1.age=24 # instance variable
# print(s1.__dict__) 
'''=>> {'name': 'Durga', 'rollno': 101, 'marks': 50, 'age': 24} '''

# s2=Student('Pavan',102)
# s2.wife="Renu"
# print(s2.__dict__)


# class Test:
#     def __init__(self) -> None:
#         self.x=10
#         self.y=20
#         self.z=30
    
#     def m1(self):
#         self.o=40

#     def m2(self):
#         self.p=50

# t1=Test()
# t1.m1()
'''total 4(3 through init and 1 through m1) instance variables will be instantiated for t1 '''
# t2=Test()
# t2.m2()
# t2.s=30
# t2.k=50
'''total 6(3 through init and 1 through m2 and 2 through s and k) instance variables will be instantiated for t1 '''
# print(t1.__dict__)
# print(t2.__dict__)
'''=>>
{'x': 10, 'y': 20, 'z': 30, 'o': 40}
{'x': 10, 'y': 20, 'z': 30, 'p': 50, 's': 30, 'k': 50}
''' 



