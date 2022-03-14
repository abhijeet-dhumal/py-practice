import mysql.connector as connector

class DBhealth:
    def __init__(self):
        self.mydb = connector.connect(host='localhost',port='3305',user='root',password='Abhijeet652@',database='python_database')
        # if no userclient table is there then will be created 
        DBhealth.create_userclient_ifNot(self)
        DBhealth.create_todo_ifNot(self)
        DBhealth.create_todo_activity_ifNot(self)
        

        print("<---------------------------------------->\n")
        print("<--Health Management System-->")

        while(True):
            try:
                print("Select Client Name: ")
                # print all possible clients using mysql
                DBhealth.fetch_all_userData(self)
                # take input for which want to do operartion 
                id = int(input("\nEnter userID : \t"))
                # print selected user 
                DBhealth.fetch_selected_userData(self,id)              

                # want to insert or retrieve the data ?
                print("\nPress 1 for User Insertion")
                print("Press 2 for Inserting activity")
                print("Press 3 for Fetch all")
                print("Press 4 for UserDeletion")
                print("Press 5 for ActivityUpdation")
                print("Press 6 for ActivityDeletion")

                op = int(input("Enter operartion to be performed from above :"))
                print("\n")
                

                if op is 1: # User insertion
                    name= input("Enter username : ")
                    query="insert into userclient(username) values('{}')".format(name)
                    cur=self.mydb.cursor()
                    cur.execute(query)
                    self.mydb.commit()
                    print('User added successfully !!!')

                if op is 2: #Fetch
                    DBhealth.fetch_todo(self)
                    todoid = int(input("\nEnter activityID from above :\t"))
                    DBhealth.fetch_selected_todo(self,todoid)
                    if todoid is 1:
                        k = 'y'
                        while (k is not "n"):
                            activity= str(input("\nEnter Exercise to be inserted : "))
                            query="insert into todo_activity values(1,'{}','Exercise',now(),'{}')".format(DBhealth.select_username(self,id),activity)
                            cur=self.mydb.cursor()
                            cur.execute(query)
                            self.mydb.commit()
                            print("Inserted Exercise Successfully!!!")
                            k = str(input("ADD MORE ? y/n:"))
                            if k =='y':
                                continue
                            else:
                                k ='n'
                                print("Thank you !!!")

                    elif todoid is 2:
                        k = 'y'
                        while (k is not "n"):
                            activity= str(input("\nEnter Diet to be inserted : "))
                            query="insert into todo_activity values(2,'{}','Diet',now(),'{}')".format(DBhealth.select_username(self,id),activity)
                            cur=self.mydb.cursor()
                            cur.execute(query)
                            self.mydb.commit()
                            print("Inserted Diet Successfully!!!")
                            k = str(input("ADD MORE ? y/n:"))
                            if k =='y':
                                continue
                            else:
                                k ='n'
                                print("Thank you !!!")

                elif op is 3: #fetch
                    DBhealth.fetch_user_activityData(self,id)
                
                elif op is 4: #user_deletion
                    DBhealth.delete_user(self,id)
                
                elif op is 5: #activity_updation
                    DBhealth.update_user_activity(self,id)
                
                elif op is 6: #activity_deletion
                    DBhealth.delete_user_activity(self,id)

                print("---------------------------------------------")

            except Exception as e:
                print("Wrong Input !!!",e)
                print("---------------------------------------------")
            
    
    # create userid if not
    def create_userclient_ifNot(self):
        query='create table if not exists userclient(userid int auto_increment,username varchar(200), primary key(userid))'
        cur=self.mydb.cursor()
        cur.execute(query)
    
    # create todo if not
    def create_todo_ifNot(self):
        query='create table if not exists todo(todoid int auto_increment,todoname varchar(50), primary key(todoid))'
        cur=self.mydb.cursor()
        cur.execute(query)
    
    # create todo if not
    def create_todo_activity_ifNot(self):
        query='create table if not exists todo_activity(todoid int auto_increment,username varchar(100),todoname varchar(50),date datetime,todo_act varchar(50), primary key(todoid))'
        cur=self.mydb.cursor()
        cur.execute(query)


    # select username
    def select_username(self,id):
        # get username from usertable
        query="select username from userclient where userid={}".format(id)
        cur=self.mydb.cursor()
        cur.execute(query) 
        for row in cur:
            return row[0]

        
    # insertion
    def insert_user(self,userid,username,phone):
        query="insert into user(userid,username,phone) values({},'{}','{}')".format(userid,username,phone)
        cur=self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        print("Client saved to database !!!")

    # fetch all 
    def fetch_all_userData(self):
        query="select * from userclient"
        cur=self.mydb.cursor()
        cur.execute(query)
        for row in cur:
            print(f"Enter {row[0]} for {row[1]}")

    # fetch selected 
    def fetch_selected_userData(self,id):
        query="select * from userclient where userid={}".format(int(id))
        cur=self.mydb.cursor()
        cur.execute(query)
        for row in cur:
            print(f"Selected client is '{row[1]}' having userID '{row[0]}' !!!")
    
    # fetch data of selected user 
    def fetch_user_activityData(self,id):
        query="select * from todo_activity where username='{}'".format(DBhealth.select_username(self,id))
        cur=self.mydb.cursor()
        cur.execute(query)
        for row in cur:
            print(row)

    

    # fetch activities among exercise and diet 
    def fetch_todo(self):
        query="select * from todo"
        cur=self.mydb.cursor()
        cur.execute(query)
        for row in cur:
            print(f"Enter {row[0]} for {row[1]}")
    
    # fetch selected exercises 
    def fetch_selected_todo(self,todoid):
        query="select * from todo where todoid={}".format(todoid)
        cur=self.mydb.cursor()
        cur.execute(query)
        for row in cur:
            print(f"Selected is '{row[1]}' having ID '{row[0]}' !!!")

    # userDeletion
    def delete_user(self, userid):
        query = "delete from userclient where userid={}".format(userid)
        cur=self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        print(f"Deleted user with userID:{userid}")

    # user_activity_updation
    def update_user_activity(self, userid):
        act= input("Enter activity which you want to update : ")
        update= input("Enter activity to update : ")
        query = "update todo_activity set {}='{}' where todo_act = '{}' ".format(str(act),str(update),str(act))
        cur=self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        print(f"Deleted entered '{act}' activity successfully !!! ")

    # user_activity_deletion
    def delete_user_activity(self, userid):
        act= input("Enter activity which you want to delete : ")
        query = "delete from todo_activity where todo_act = '{}' ".format(str(act))
        cur=self.mydb.cursor()
        cur.execute(query)
        self.mydb.commit()
        print(f"Deleted entered '{act}' activity successfully !!! ")



helper=DBhealth()
print(helper) 


