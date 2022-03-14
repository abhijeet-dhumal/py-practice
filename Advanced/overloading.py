'''
class 
object 
Reference
types of methods constructors
self variable 
inner classes 
how to access memebrs of one class from other class 
GC & destructors 
-------------------------------------------------------
Polymorphism
---------------
Duck typing philosophy of python 
Overloading :
    operator overloading 
    Method overloading
    Constructor overloading 
Overriding :
    Method overrding
    constructor overriding 
--------------------------------------------------------
Data hiding 
abstraction
'''

'''
Polymorphism --> Poly means many, morphs means forms 
    one name but multiple forms 

overloading --> 
    operator overloading: 
        same operator but different behaviours at different arguments
        10+20==>30 
        "Durga"+"Soft"==>"DurgaSoft"
        2*3==>6 
        "Durga"*3==>"DurgaDurgaDurga"
        
        - operator overloading by using magic methods 
        - ====>__add__

+==> __add__()
-==> __sub__()
/==> __div__()
*==> __mul__()
%==> __mod__()
//==> __floordiv__()
**==> __pow__()

+=   => __iadd__()
-=   => __isub__()
/=   => __idiv__()
*=   => __imul__()
%=   => __imod__()
//=   => __ifloordiv__()
**=   => __ipow__()

>   => __gt__()
>=   => __ge__()
<   => __lt__()
<=   => __le__()
==   => __eq__()
!=   => __ne__()

'''
# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):  #magic method ,self=b1, other=b2
#         return self.pages+other.pages
#     def __mul__(self,other):  #magic method ,self=b1, other=b2
#         return self.pages*other.pages
#     def __sub__(self,other):  #magic method ,self=b1, other=b2
#         return self.pages-other.pages
#     def __div__(self,other):  #magic method ,self=b1, other=b2
#         return self.pages/other.pages

# b1=Book(100)
# b2=Book(200)
# b3=Book(700)
'''Python will give left and right we are adding objects
To make this operation possible we have to use magic method __add__'''
# print(b1+b2) #=>>300
# print(b1+b3) #=>>800
# print(b2+b3) #=>>900

# print(b1+b2+b3) 
'''=>> Unsupported operand type for +: 'int' and 'Book' '''


# class Book:
#     def __init__(self,pages):
#         self.pages=pages 
    
#     def __str__(self) -> str:
#         # return "Durga"
#         return "The number of pages: "+str(self.pages)


#     def __add__(self,other):
#         # return self.pages+other.pages
#         total= self.pages+other.pages
#         b=Book(total)
#         return b

# b1=Book(300)
# print(b1) 
'''
# By default this print object statement calls string method  
#=>> <__main__.Book object at 0x018505F0>
# In case you dont want this kind of error you can use '__str__' magic method
'''
# print(b1)
'''=>> Durga'''
# b2=Book(200)
# print(b1+b2) 
'''=>> unsupported operand type(s) for +: 'Book' and 'Book'  
To minimize this error you can use __add__ magic method '''
# print(b1+b2) 
'''=>> 500'''
# b3=Book(100)
# print(b1+b2+b3)
'''=>> unsupported operand type(s) for +: 'int' and 'Book'
this print statement considering first two summation as int object but b3 as Book object ,
to overcome with this we have to do some changes in str magic method
'''
# print(b1+b2+b3) # B(300)+B(300)

#=>> The number of pages : 600 

# <<---------------------------------------------------------------------------->> 
'''
    method overloading: same method name but different arguments 
        in python method overloading concept is not available 
        it will always override first method with second
        deposit(cash)
        deposit(cheque)
        deposit(dd)

'''