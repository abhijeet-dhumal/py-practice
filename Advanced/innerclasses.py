'''
Inner class:
    without existing one type of object if 
    there is no chance of existing anoter type of 
    object then we should go for inner class.

'''
# class Outer:
#     class Inner :
#         def m1(self):pass 

# o=Outer()
# i=o.Inner()
# i.m1()
'''or'''
# Outer().Inner().m1()


# class Person:
#     def __init__(self) -> None:
#         self.name="Abhi"
#         self.dob=self.DOB()

#     def display(self):
#         print('Name : ',self.name)
#         self.dob.display() 

#     class DOB:
#         def __init__(self) -> None:
#             self.dd=15 
#             self.mm=8 
#             self.yyyy=1947 

#         def display(self):
#             print(f"Date of birth : {self.dd}/{self.mm}/{self.yyyy}")

# p=Person()
# p.display()
'''=>>
Name :  Abhi
Date of birth : 15/8/1947
'''
# p.DOB().display()
'''=>>
Date of birth : 15/8/1947
'''

# class Human:
#     def __init__(self) -> None:
#         self.name="Abhi"
#         self.head=self.Head()

#     def display(self):
#         print(f"Name : {self.name}")
#         self.head.talk()
#         self.head.brain.think()
    
#     class Head:
#         def __init__(self) -> None:
#             self.brain=self.Brain()

#         def talk(self):
#             print("Talking...")
        
#         class Brain:
#             def think(self):
#                 print("Thinking...")

# n=Human()
# n.display()
'''=>>
Name : Abhi
Talking...
Thinking...
'''

# class Test:
#     '''inner methods'''
#     def m1(self):
#         global sum
#         def sum(a,b):
#             print(f'First arg : {a}')
#             print(f'2nd arg : {b}')
#             print(f'Sum of args : {a+b}')
#         '''code reusability'''
#         sum(10,20)
#         sum(100,200)

# # Test().m1()
'''=>>
First arg : 10
2nd arg : 20
Sum of args : 30
First arg : 100
2nd arg : 200
Sum of args : 300
'''