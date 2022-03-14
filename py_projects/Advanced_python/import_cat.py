import cat
from cat import Cat

# use imported class 

if __name__ == '__main__':
    def test():
        b= Cat('kitty',2)
        c= Cat('perry',3)
        print(b)
        print(c)
        b.description()
        c.description()

        c.meow()
        b.meow()
        c.hungry()

    print(test()) 
    x=Cat('test',20)
    print(x)
    