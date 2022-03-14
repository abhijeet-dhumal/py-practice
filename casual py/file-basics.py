# file io basics
"""
"r"-open file for reading
"w"- open file for writing
"x"-create a file if not exists
"a"- add more content to a file
"t"-text mode
"b"- binary mode
"+"- read and write
"""

#to access docstring in functions:
def function1(a,b):
    """to print average of two numbers..."""
    average=(a+b)/2
    return average
v=function1(5,7)
print(v)
print(function1.__doc__)