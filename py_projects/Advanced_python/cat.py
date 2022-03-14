# self is the first param 
# instance = created 

class Cat:
    name=''
    age=2
    color=''

    def __init__(self,name,age,color='white'):  #constructor which will run each time when class is called 
        self.name=name
        self.age=age
        self.color=color
        print(f'Constructor for {self.name}')

    def meow(self):
        print(f'{self.name}meow')

    def sleep(self):
        print(f'{self.name} zzz')
        
    def hungry(self):
        for i in range(5):
            self.meow()

    def description(self):
        print(f'{self.name} is a {self.color} cat and {self.age} years old... ')
