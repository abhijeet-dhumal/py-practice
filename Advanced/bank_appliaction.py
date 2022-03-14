import sys
class Customer:
    '''Customer class with bank related operations'''
    bankname="DurgaBank"

    def __init__(self,name,balance=0) -> None:
        self.name=name 
        self.balance=balance

    @staticmethod
    def menu():
        menu={1:"Deposit",2:"Withdraw",0:"Exit"}
        print("\\"*20)
        for key,value in menu.items():
            print(f"Enter '{key}' to '{value}' ")
        print("/"*20)

    def deposit(self,amount):
        self.balance+=amount
        print(f"After deposit the balance : {self.balance}")

    def withdraw(self,withdrawl_amount):
        if withdrawl_amount>self.balance:
            print("Insufficient balance ...Cannot perform this operation !!!")
            print("_"*20)
            sys.exit()
        else:
            self.balance-=withdrawl_amount

        print(f"After withdrawl the balance : {self.balance}")

print("\n","*"*20)
print(f"Welcome to ' {Customer.bankname} '")   
name=input("Enter your name : ")
customer1=Customer(name)
Boolean=True
while Boolean:
    customer1.menu()
    op=int(input("Enter Operation to be performed:"))
    if op==1:
        amount=int(input("Enter amount to deposit : "))
        customer1.deposit(amount)
    elif op==2:
        amount=int(input("Enter amount to withdraw : "))
        customer1.withdraw(amount)

    elif op==0:
        print(f"Thanks for using our services '{name}' !!!")
        print("*"*20)
        Boolean=False
    else:
        print("Choose valid option !!!")    
