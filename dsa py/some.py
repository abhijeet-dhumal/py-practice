testcase1={
    'input':{
        'usernames':['Nikhil','Suresh','Akshay'],
        'names':['Nikhil','Suresh','Akshay'],
        'emails':['Nikhil@gmail.com','Suresh@gmail.com','Akshay@gmail.com'],
    },
    'output':5
}

class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
        
    def __repr__(self):
        return f"User(username={self.username}, name={self.name}, email={self.email}"
    def __str__(self):
        return self.__repr__()
        
class UserDatabase:
    def __init__(self):
        self.users=[]

    def insert(self,user):
        i=0
        while i<len(self.users):
            # find the first username greater than the new user's username 
            if self.users[i].username>user.username:
                break
            i+=1
                
        self.users.insert(i,user)
        print(self.users)

    def find(self,username):
        for user in self.users:
            if user.username==username:
                return self.users.index(user),user

    def update(self,user):
        target=self.find(user)
        target.name,target.email=user.name,user.email

    def list_all(self):
        return self.users

jhonny=User('Jhonny','Jagdish chandra','johnny@gmail.com')
lila=User('lila','lolita gandhi','lolita@gmail.com')
kalpesh=User('kalpesh','kalpesh chawla','kalpesh@gmail.com')
gajju=User('Gajju','Gajju More','Gajju@gmail.com')
users_list=[jhonny,lila,kalpesh,gajju]

print(jhonny.name)
database=UserDatabase()
database.insert(jhonny)
database.insert(lila)
# database.insert('abhijeet')
# database.insert('suresh')
# database.insert('sukhi')
# print(database.find('sukhi'))