
books_dic = ['flame','blaze','shatif']
temp = {'flame':'Arjun'}
available_books = ['blaze','shatif']
op = {1:'Display entered book,',2:'Lend book,',3:'Add a book,',4:'Return a book .'}

class Library :
    # for using this class library ,create object and run it using selction function 

    def __init__(self, book_name ):
        self.bookname = book_name

    def selection(self):
        while True:
            for key,value in op.items():
                print(f"Enter {key} for {value}")
            dp= int(input('Enter operation you want to perform : ' ))
            if dp == 1:
                print(self.display())
            elif dp == 2:
                bookname = input('Enter bookname that you wish to retrive : ')
                print(self.lend(bookname))
            elif dp == 3:
                bookname = input('Enter bookname that you wish to add : ')
                print(self.add(bookname))
            elif dp == 4:
                bookname = input('Enter bookname that you wish to return : ')
                print(self.re_turn(bookname))
            else :
                print('Please enter valid input !!!')

    def display(self):
        print('<------------------------------------------------> \n')
        print("The books are as follows : ")
        for i in books_dic:
            print(f"{i}," ,end=" ")
        print("\n \nThe books available are as follows : ")
        for i in available_books:
            print(f"{i}," ,end=" ")
        return '\n \n<------------------------------------------------>'

    def lend(self, book):
        print('<------------------------------------------------> \n')
        if self.bookname in books_dic:
            if (self.bookname in available_books):
                name = input("Enter your name : ")
                available_books.remove(self.bookname)
                temp[ self.bookname ] = name
                return f"This {self.bookname} book is available !!! {available_books} {temp}\n<------------------------------------------------>"
            else:
                return f'Srry, {self.bookname} book is Currently unavailable!!! \nThe current author of this \'{self.bookname}\' book is \'{temp.get(self.bookname)}\' \n \n<------------------------------------------------> '

    def add(self, book):
        print('<------------------------------------------------> \n')
        if self.bookname in books_dic:
            if (self.bookname in available_books):
                return f" This {self.bookname} book is already in Library !!! \n   \n<------------------------------------------------>"
            else:
                available_books.append(self.bookname)
                
                return f' This {self.bookname} is Successfully added in Library !!! \n {available_books}\n<------------------------------------------------> '

    def re_turn(self, book):
        print('<------------------------------------------------> \n')
        if self.bookname in books_dic:
            if (self.bookname in available_books):
                return f" This {self.bookname} book is already present in Library !!!\n<------------------------------------------------>"
            else:
                del temp[ self.bookname ]  
                available_books.append(self.bookname)
                print(f"This {self.bookname} book is returned Successfully in Library !!! ")
                return f'{temp}\n {available_books}\n<------------------------------------------------> '



abhi = Library('fs')
print(abhi.selection())