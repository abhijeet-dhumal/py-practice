
books_dic = ['flame','blaze','shatif']
temp = {'flame':'Arjun'}
available_books = ['blaze','shatif']
op = {1:'Display books,',2:'Lend book,',3:'Add a book,',4:'Return a book .'}

class Library :

    def selection(self,book):
        n = True
        while n==True:
            for key,value in op.items():
                print(f"Enter {key} for {value}")
            dp= int(input('Enter operation you want to perform : ' ))
            if dp == 1:
                print(self.display())
            elif dp == 2:
                print(self.lend(book))
            elif dp == 3:
                print(self.add(book))
            elif dp == 4:
                print(self.re_turn(book))
            else :
                print('Please enter valid input !!!')
            p = input('\n Do you want to enter again (y/n) ? : ')
            if p == 'y':
                n = True 
                continue
            else:
                n = False 
                return f'Thank you for using our services !!! \n \n <------------------------------------------------> \n'
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
        if book in books_dic:
            if (book in available_books):
                name = input("Enter your name : ")
                available_books.remove(book)
                temp[ book ] = name
                return f"This {book} book is available !!! {available_books} {temp} \n \n<------------------------------------------------>"
            else:
                return f'Srry, {book} book is Currently unavailable!!! \nThe current author of this \'{book}\' book is \'{temp.get(book)}\' \n \n<------------------------------------------------> '

    def add(self, book):
        print('<------------------------------------------------> \n')
        if (book in available_books):
            return f" This \'{book}\' book is already in Library !!!  \n<------------------------------------------------>"
        else:
            available_books.append(book)
            return f' This \'{book}\' is Successfully added in Library !!! \n Now available books are {available_books}\n \n<------------------------------------------------> '

    def re_turn(self, book):
        print('<------------------------------------------------> \n')
        if (book in available_books):
            return f" This \'{book}\' book is already present in Library !!! \n \n<------------------------------------------------>"
        elif (book not in available_books):
            del temp[ book ]  
            available_books.append(book)
            print(f"This \'{book}\' book is returned Successfully in Library !!! ")
            return f'Now available books are {available_books}\n \n<------------------------------------------------> '


# while True:
#     for key,value in op.items():
#         print(f"Enter {key} for {value}")
#     dp= int(input('Enter operation you want to perform : ' ))
#     if dp == 1:
#         abhi = Library('fs')
#         print(abhi.display())
#     elif dp == 2:
#         bookname = input('Enter bookname that you wish to retrive : ')
#         abhi = Library(bookname)
#         print(abhi.lend(bookname))
#     elif dp == 3:
#         bookname = input('Enter bookname that you wish to add : ')
#         abhi = Library(bookname)
#         print(abhi.add(bookname))
#     elif dp == 4:
#         bookname = input('Enter bookname that you wish to return : ')
#         abhi = Library(bookname)
#         print(abhi.re_turn(bookname))
#     else :
#         print('Please enter valid input !!!')


book = input('Enter bookname : ')
abhi = Library()
print(abhi.selection(book))