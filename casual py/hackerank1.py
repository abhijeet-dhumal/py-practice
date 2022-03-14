class Item:
    # Implement the Item here
    def __init__(self,name,price):
        self.name=name 
        self.price=price 
        pass


class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        pass
    def add(self,item):
        self.item=item
        pass 
    def total(self):
        summ=0  
        for i in self:
            summ+=i
        return summ
        # for i in self.item():
        #     pass
        pass
    

if __name__ == '__main__':
    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            print(str(len(cart)) + "\n")
        elif command == "total":
            print(cart.total() + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
