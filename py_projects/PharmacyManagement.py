print("======Pharmacy OPERATION System=====")
import mysql.connector as mysql
conn=mysql.connect(host="localhost",user="root",password="",database="PharmacyManagement")
cursor=conn.cursor()

def createTableIfNot():
    query="create table if not exists medicine(Entryno int auto_increment,Medicine varchar(100),Price varchar(50), Quantity varchar(10), primary key(Entryno)) "
    cursor.execute(query)

createTableIfNot()

def insert():
    Medicine=input("Enter your medicine name: ")
    Price=input("Enter Price: ")
    Quantity=input("Enter Quantity: ")
    sql="insert into medicine (Medicine, Price, Quantity) values(%s,%s,%s)"
    val=(Medicine, Price, Quantity)
    try:
        cursor.execute(sql,val)
        conn.commit()
        print("Successful")
        menu()
    except Exception as e: 
        print(e)
        menu()
def read():
    sql="select * from medicine"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for x in data:
            print(x)
        print("successful")
        menu()
    except:
        print("Error occured")
        menu()
def delete():
    ch=input("Do u have Entry no.?(y/n)").lower()
    if(ch=='y'):
        Entryno=input("Enter your entry no. : ")
        sql="delete from medicine where Entryno=%s"
        val=(Entryno,)
        try:
            cursor.execute(sql,val)
            conn.commit()
            print("Successful")
            menu()
        except:
            print("Error")
            menu()
    else:
        print("Go to read section and get your entry no.")
        menu()
        #

        
def update():
    ch=input("Do u have entry no.?(y/n): ").lower()
    if(ch=='y'):
        Entryno=input("Enter your entry no.: ")
        sql="select * from medicine where Entryno=%s"
        val=(Entryno,)
        try:
            cursor.execute(sql,val)
            data=cursor.fetchall()
            for x in data:
            
                Medicine=x[1]
                Price=x[2]
                Quantity=x[3]
            print("1.update Medicine\n2.update Price\n3.update Quantity")
            ch=int(input("Enter your choice: "))
            if(ch==1):
                Medicine=input("Enter your new Name: ")
            elif(ch==2):
                Price=input("Enter your new price: ")

            elif(ch==3):
                Quantity=input("Enter your new quantity: ")


            else:
                print("wrong input")
                menu()
            sql="update medicine set Medicine=%s, Price=%s, Quantity=%s where Entryno=%s"
            val=(Medicine,Price, Quantity,Entryno)
            try:
                cursor.execute(sql,val)
                conn.commit()
                print("Successful")
                menu()
            except Exception as e:
                print("error")
                menu()
        except Exception as e:
            print(e)
            menu()

        
        #
def menu():
    print("Select any option\n1. Insert\n2. Read\n3.Update\n4. Delete")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        insert()
    elif(ch==2):
        read()
    elif(ch==3):
        update()
    elif(ch==4):
        delete()
    else:
        print("Wrong input choosen")
        menu()
menu()
