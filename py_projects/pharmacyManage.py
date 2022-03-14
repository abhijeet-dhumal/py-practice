from tkinter import *
from tkinter import messagebox
import os
root = Tk()
root.title("Simple Pharmacy Managment System")
root.configure(width=1500,height=600,bg='BLACK')
var=-1

import mysql.connector as connector
mydb = connector.connect(host='localhost',port='3305',user='root',password='Abhijeet652@',database='pharmacy_management')
# create userid if not
def create_medicine_table_ifnot():
    query='create table if not exists medicines(medid int(10) auto_increment,medname varchar(200),medprice int(10),medquantity int(5)medcategory varchar(100),meddiscount int(3), primary key(medid))'
    cur=mydb.cursor()
    cur.execute(query)

def addMedicine(medName,medPrice,medQuan,medCategory,medDisc):
    query="insert into medicines(medname,medprice,medquantity,medcategory,meddiscount) values('{}',{},{},'{}',{})".format(str(medName),medPrice,medQuan,str(medCategory),medDisc)
    cur=mydb.cursor()
    cur.execute(query)
    mydb.commit()

def deleteMedicine(medName):
    query = "delete from medicines where medname='{}'".format(str(medName))
    cur=mydb.cursor()
    cur.execute(query)
    mydb.commit()
    print(f"Deleted medicine with name:{medName}")

def update_medicine(medName,medNameA,medPrice,medPriceA,medQuan,medQuanA,medCategory,medCategoryA,medDisc,medDiscA):
    query = "update medname set medname='{}', medprice set {}={}, medquantity set {}={}, medcategory set {}='{}', meddiscount set {}={}, where medname = '{}' ".format(str(medName),str(medNameA),medPrice,medPriceA,medQuan,medQuanA, str(medCategory),str(medCategoryA),medDisc,medDiscA,str(medName))
    cur=mydb.cursor()
    cur.execute(query)
    mydb.commit()
    print(f"Updated entered '{medName}' medicine successfully !!! ")   



def additem():
    try:
        medid=entry1.get()
        medName=entry2.get()
        medPrice=entry3.get()
        medQuan=entry4.get()
        medCategory=entry5.get()
        medDisc=entry6.get()
            
        create_medicine_table_ifnot()
        addMedicine(medName,medPrice,medQuan,medCategory,medDisc)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)

    except Exception as e:
        print(e)


def deleteitem():
    medName=entry1.get()
    try:                
        create_medicine_table_ifnot()
        deleteMedicine(medName)
        entry1.delete(0, END)

    except Exception as e:
        print(e)

def firstitem():
    query="select * from medicines where medid={}".format(1)
    cur=mydb.cursor()
    cur.execute(query)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    for row in cur:
        entry1.insert(0,str(row[0]))
        entry2.insert(0,str(row[1]))
        entry3.insert(0,str(row[2]))
        entry4.insert(0,str(row[3]))
        entry5.insert(0,str(row[4]))
        entry6.insert(0,str(row[5]))

def nextitem():
    try:
        medid=entry1.get()
        nextmedid=int(medid)+1
        query="select * from medicines where medid={}".format(nextmedid)
        cur=mydb.cursor()
        cur.execute(query)
        entry1.delete(0, END)
        for row in cur:
            print(row)
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)
            entry1.insert(0,str(row[0]))
            entry2.insert(0,str(row[1]))
            entry3.insert(0,str(row[2]))
            entry4.insert(0,str(row[3]))
            entry5.insert(0,str(row[4]))
            entry6.insert(0,str(row[5]))
            
            
    except Exception as e:
        messagebox.showinfo(f"Title:", f"SORRY!...NO MORE RECORDS ,{e}")

def previousitem():
    try:
        medid=entry1.get()
        prevmedid=int(medid)-1
        if(prevmedid>0):
            query="select * from medicines where medid={}".format(prevmedid)
        cur=mydb.cursor()
        cur.execute(query)
        entry1.delete(0, END)
        for row in cur:
            print(row)
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)
            entry1.insert(0,str(row[0]))
            entry2.insert(0,str(row[1]))
            entry3.insert(0,str(row[2]))
            entry4.insert(0,str(row[3]))
            entry5.insert(0,str(row[4]))
            entry6.insert(0,str(row[5]))
            
            
    except Exception as e:
        messagebox.showinfo(f"Title:", f"SORRY!...NO MORE RECORDS ,{e}")

def lastitem():
    try:
        id="select max(medid) from medicines"
        idcur=mydb.cursor()
        idcur.execute(id)
        for id in idcur:
            lastid=id[0]
        query="select * from medicines where medid={}".format(lastid)
        cur=mydb.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)

            entry1.insert(0,str(row[0]))
            entry2.insert(0,str(row[1]))
            entry3.insert(0,str(row[2]))
            entry4.insert(0,str(row[3]))
            entry5.insert(0,str(row[4]))
            entry6.insert(0,str(row[5]))

    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")


def updateitem():
    medid=entry1.get()
    medName=entry2.get()
    medPrice=entry3.get()
    medQuan=entry4.get()
    medCategory=entry5.get()
    medDisc=entry6.get()

    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)

    medidA=entry1.get()
    medNameA=entry2.get()
    medPriceA=entry3.get()
    medQuanA=entry4.get()
    medCategoryA=entry5.get()
    medDiscA=entry6.get()
    
    update_medicine(medName,medNameA,medPrice,medPriceA,medQuan,medQuanA,medCategory,medCategoryA,medDisc,medDiscA)


def searchitem():
    try:
        medName=entry2.get()
        query="select * from medicines where medname='{}'".format(medName)
        cur=mydb.cursor()
        cur.execute(query)
        for row in cur:
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(row[0]))
            entry2.insert(0, str(row[1]))
            entry3.insert(0, str(row[2]))
            entry4.insert(0, str(row[3]))
            entry5.insert(0, str(row[4]))
            entry6.insert(0, str(row[5]))

    except:
        messagebox.showinfo("Title", "No outcomes found for you search !!!")



def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


label0= Label(root,text="PHARMACY MANAGEMENT SYSTEM ",bg="black",fg="white",font=("Times", 30))
label1=Label(root,text="MedicineID",bg="red",relief="ridge",fg="white",font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 12))
label2=Label(root,text="ENTER ITEM NAME",bg="red",relief="ridge",fg="white",font=("Times", 12),width=25)
entry2=Entry(root , font=("Times", 12))
label3=Label(root, text="ENTER ITEM PRICE",bd="2",relief="ridge",height="1",bg="red",fg="white", font=("Times", 12),width=25)
entry3= Entry(root, font=("Times", 12))
label4=Label(root, text="ENTER ITEM QUANTITY",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
entry4= Entry(root, font=("Times", 12))
label5=Label(root, text="ENTER ITEM CATEGORY",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
entry5= Entry(root, font=("Times", 12))
label6=Label(root, text="ENTER ITEM DISCOUNT",bg="red",relief="ridge",fg="white", font=("Times", 12),width=25)
entry6= Entry(root, font=("Times", 12))

button1= Button(root, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12),command=additem)
button2= Button(root, text="DELETE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=deleteitem)
button3= Button(root, text="VIEW FIRST ITEM" , bg="white", fg="black", width =20, font=("Times", 12),command=firstitem)
button4= Button(root, text="VIEW NEXT ITEM" , bg="white", fg="black", width =20, font=("Times", 12), command=nextitem)
button5= Button(root, text="VIEW PREVIOUS ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=previousitem)
button6= Button(root, text="VIEW LAST ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=lastitem)
button7= Button(root, text="UPDATE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=updateitem)
button8= Button(root, text="SEARCH ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=searchitem)
button9= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12),command=clearitem)

label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)
label6.grid(row=6,column=0, sticky=W, padx=10, pady=10)
entry1.grid(row=1,column=1, padx=40, pady=10)
entry2.grid(row=2,column=1, padx=10, pady=10)
entry3.grid(row=3,column=1, padx=10, pady=10)
entry4.grid(row=4,column=1, padx=10, pady=10)
entry5.grid(row=5,column=1, padx=10, pady=10)
entry6.grid(row=6,column=1, padx=10, pady=10)
button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=1,column=5, padx=40, pady=10)
button3.grid(row=2,column=4, padx=40, pady=10)
button4.grid(row=2,column=5, padx=40, pady=10)
button5.grid(row=3,column=4, padx=40, pady=10)
button6.grid(row=3,column=5, padx=40, pady=10)
button7.grid(row=4,column=4, padx=40, pady=10)
button8.grid(row=4,column=5, padx=40, pady=10)
button9.grid(row=5,column=5, padx=40, pady=10)
root.mainloop()
