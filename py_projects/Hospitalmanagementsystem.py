import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter.constants import BOTTOM, LEFT, RIGHT
from tkinter.font import BOLD

import mysql.connector
mydb=mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Abhijeet652@",
                            database="hospital_mgmt",
                            port="3305"
)
# if no userclient table is there then will be created 
# create userid if not
def create_appointments_ifNot():
    query='create table if not exists appointments(appointment_id int(5) auto_increment,patientname varchar(200),age int(3),gender varchar(20),contact varchar(12),date datetime,doctorname varchar(100), primary key(appointment_id))'
    cur=mydb.cursor()
    cur.execute(query)

create_appointments_ifNot()
# create userid if not
def create_patients_ifNot():
    query='create table if not exists patients(patient_id int(5) auto_increment,patientname varchar(200),age int(3),gender varchar(20), contact varchar(12),email varchar(100),permanentadd varchar(200),marital varchar(20),prevmedrecords varchar(200), primary key(patient_id))'
    cur=mydb.cursor()
    cur.execute(query)
create_patients_ifNot()

# create doctrs if not
def create_doctors_ifNot():
    query='create table if not exists doctors(doctor_id int(5) auto_increment,doctorname varchar(200),gender varchar(20), contact varchar(10),availtime datetime,specialize varchar(100), primary key(doctor_id))'
    cur=mydb.cursor()
    cur.execute(query)
create_doctors_ifNot()

# create doctrs if not
def create_billing_ifNot():
    query='create table if not exists billing(billing_id int auto_increment,bedno int,patientname varchar(200),admitdate datetime ,dischargedate datetime ,mobile int,medicine varchar(100) ,totalamount int, primary key(billing_id))'
    cur=mydb.cursor()
    cur.execute(query)
create_billing_ifNot()

def addAppointment(patientname,age,gender,contact,date,doctorname):
    try:
        query="insert into appointments(patientname,age,gender,contact,date,doctorname) values('{}',{},'{}','{}',now(),'{}')".format(patientname,age,gender,str(contact),date,doctorname)
        cur=mydb.cursor()
        cur.execute(query)
        mydb.commit()
        print("Appointment added successfully!!!")
        messagebox.showinfo(f"Title:",f"Appointment for patient {patientname} is added successfully !!!")

    except Exception as e:
        messagebox.showinfo(f"Title:", f"SORRY!... ,{e}")
        print(e)

def updateAppointment(patientname,age,gender,contact,date,doctorname):
    try:
        print(patientname,age,gender,contact,date,doctorname)
        query = "update appointments set patientname='{}', age={}, gender ='{}', contact ='{}', date = now(),doctorname='{}' where patientname = '{}' ".format(patientname,age,gender,contact,doctorname,patientname)
        cur=mydb.cursor()
        cur.execute(query)
        mydb.commit()
        print(f"Updated entered '{patientname}' patient successfully !!! ")  
        messagebox.showinfo(f"Title:",f"Appointment for patient {patientname} is updated successfully !!!") 
    except Exception as e:
        messagebox.showinfo(f"Title:", f"SORRY!... ,{e}")
        print(e)

def deleteAppointment(patientname):
    try:
        query = "delete from appointments where patientname='{}'".format(str(patientname))
        cur=mydb.cursor()
        cur.execute(query)
        mydb.commit()
        print(f"Deleted medicine with name:{patientname}")
        messagebox.showinfo(f"Title:",f"Appointment for patient {patientname} is deleted successfully !!!") 

    except Exception as e:
        messagebox.showinfo(f"Title:", f"SORRY!... ,{e}")
        print(e)


root=Tk()
root.geometry("1500x800")
root.title("HOSPITAL MANAGEMENT SYSTEM")
lbl=Label(root,text="IMPERIAL MULTISPECIALITY HOSPITAL",bd=20,relief=RIDGE,fg="black",bg="Yellow",font=("times new roman",40,"bold"))
lbl.pack(side=TOP,fill=Y)

def next():
    nx=Tk()
    nx.title("Appointments")
    nx.geometry("650x500+450+150")
    nx.maxsize(650,500)
    nx.minsize(650,500)
    lbl=Label(nx,text="APPOINTMENTS",bd=20,relief=SUNKEN,fg="black",bg="white",font=("times new roman",20,BOLD)).pack()
    label1=tkinter.Label(nx,text="Patient Name :-",font=("arialbold",10,BOLD)).place(x=10,y=80)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=120,y=80)
    label2=tkinter.Label(nx,text="Age :-",font=("arialbold",10,BOLD)).place(x=10,y=120)
    entry2=Entry(nx,relief="sunken",bd=2)
    entry2.place(x=120,y=120)
    label3=tkinter.Label(nx,text="Gender :-",font=("arialbold",10,BOLD)).place(x=10,y=160)
    # var=IntVar()
    # r1=Radiobutton(nx,text="male",variable=var,value=0,command=set)
    # r1.place(x=120,y=160)
    # r1=Radiobutton(nx,text="female",variable=var,value=1,command=set)
    # r1.place(x=180,y=160)
    entry3=Entry(nx,relief="sunken",bd=2)
    entry3.place(x=120,y=160)
    label4=tkinter.Label(nx,text="Contact Number :-",font=("arialbold",10,BOLD)).place(x=10,y=200)
    entry4=Entry(nx,relief="sunken",bd=2)
    entry4.place(x=120,y=200)
    label5=tkinter.Label(nx,text="Date & Time :-",font=("arialbold",10,BOLD)).place(x=10,y=240)
    entry5=Entry(nx,relief="sunken",bd=2)
    entry5.place(x=120,y=240)
    label6=tkinter.Label(nx,text="Doctors Name :-",font=("arialbold",10,BOLD)).place(x=10,y=280)
    entry6=Entry(nx,relief="sunken",bd=2)
    entry6.place(x=120,y=280)

    def additem():
        try:
            patientname=entry1.get()
            age=entry2.get()
            gender=entry3.get()
            contact=entry4.get()
            date=entry5.get()
            doctorname=entry6.get()
            print(patientname,age,gender,contact,date,doctorname)    
            create_appointments_ifNot()
            addAppointment(patientname,age,gender,contact,date,doctorname)
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)

        except Exception as e:
            messagebox.showinfo(f"Title:", f"SORRY!... ,{e}")

    
    def updateitem():
        patientname=entry1.get()
        age=entry2.get()
        gender=entry3.get()
        contact=entry4.get()
        date=entry5.get()
        doctorname=entry6.get()
        
        updateAppointment(patientname,age,gender,contact,date,doctorname)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)

    def deleteitem():
        patientname=entry1.get()                
        create_appointments_ifNot()
        deleteAppointment(patientname)
        entry1.delete(0, END)

        
    def clearitem():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)

    button1=Button(nx,text="SCHEDULE",fg="white",bg="black",font=("arialbold",10),command=additem)
    button1.place(x=20,y=350)
    button2=Button(nx,text="UPDATE",fg="white",bg="black",font=("arialbold",10),command=updateitem)
    button2.place(x=150,y=350)
    button3=Button(nx,text="DELETE",fg="white",bg="black",font=("arialbold",10),command=deleteitem)
    button3.place(x=270,y=350)
    button4=Button(nx,text="CLEAR",fg="white",bg="black",font=("arialbold",10),command=clearitem)
    button4.place(x=390,y=350)
      
bt1=tkinter.Button(root,text="Appointments",fg="white",bg="black",font=("arialbold",30),command=next)
bt1.place(x=20,y=200)

def next1():
    nx=Tk()
    nx.title("Patients Details")
    nx.geometry("650x500+450+150")
    nx.maxsize(650,500)
    nx.minsize(650,500)
    lbl=Label(nx,text="PATIENT DETAILS",bd=20,relief=SUNKEN,fg="black",bg="white",font=("times new roman",20,BOLD)).pack()
    label=tkinter.Label(nx,text="Patient Name :-",font=("arialbold",10,BOLD)).place(x=10,y=80)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=150,y=80)
    label=tkinter.Label(nx,text="Age :-",font=("arialbold",10,BOLD)).place(x=10,y=120)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=150,y=120)
    label=tkinter.Label(nx,text="Gender :-",font=("arialbold",10,BOLD)).place(x=10,y=160)
    var=IntVar()
    r1=Radiobutton(nx,text="male",variable=var,value=0,command=set)
    r1.place(x=150,y=160)
    r1=Radiobutton(nx,text="female",variable=var,value=1,command=set)
    r1.place(x=220,y=160)
    label=tkinter.Label(nx,text="Contact Number :-",font=("arialbold",10,BOLD)).place(x=10,y=200)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=150,y=200)
    label=tkinter.Label(nx,text="email address :-",font=("arialbold",10,BOLD)).place(x=10,y=240)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=150,y=240)
    label=tkinter.Label(nx,text="permanant address :-",font=("arialbold",10,BOLD)).place(x=10,y=280)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=150,y=285)
    label=tkinter.Label(nx,text="Marital Status :-",font=("arialbold",10,BOLD)).place(x=10,y=320)
    var=IntVar()
    r1=Radiobutton(nx,text="Married",variable=var,value=0,command=set)
    r1.place(x=150,y=321)
    r1=Radiobutton(nx,text="Unmarried",variable=var,value=1,command=set)
    r1.place(x=230,y=321)
    label=tkinter.Label(nx,text="Patient ID :-",font=("arialbold",10,BOLD)).place(x=10,y=360)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=150,y=364)
    label=tkinter.Label(nx,text="Privious Medical \nrecords :-",font=("arialbold",10,BOLD)).place(x=10,y=400)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=150,y=420)
    bt=Button(nx,text="UPDATE",fg="white",bg="black",font=("arialbold",10))
    bt.place(x=20,y=460)
    bt=Button(nx,text="DELETE",fg="white",bg="black",font=("arialbold",10))
    bt.place(x=250,y=460)
    
bt2=tkinter.Button(root,text="Patients Details",fg="white",bg="black",font=("arialbold",30),command=next1)
bt2.place(x=20,y=300)

def next2():
    nx=Tk() 
    nx.title("Doctors Details")
    nx.geometry("650x500+450+150")
    nx.maxsize(650,500)
    nx.minsize(650,500)
    lbl=Label(nx,text="DOCTORS DETAILS",bd=20,relief=SUNKEN,fg="black",bg="white",font=("times new roman",20,BOLD)).pack()
    label=tkinter.Label(nx,text="Doctors Name :-",font=("arialbold",10,BOLD)).place(x=10,y=80)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=170,y=80)
    label=tkinter.Label(nx,text="Doctors ID :-",font=("arialbold",10,BOLD)).place(x=10,y=120)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=170,y=120)
    label=tkinter.Label(nx,text="Gender :-",font=("arialbold",10,BOLD)).place(x=10,y=160)
    var=IntVar()
    r1=Radiobutton(nx,text="male",variable=var,value=0,command=set)
    r1.place(x=170,y=160)
    r1=Radiobutton(nx,text="female",variable=var,value=1,command=set)
    r1.place(x=230,y=160)
    label=tkinter.Label(nx,text="Contact Number :-",font=("arialbold",10,BOLD)).place(x=10,y=200)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=170,y=200)
    label=tkinter.Label(nx,text="Day & avaibility Time :-",font=("arialbold",10,BOLD)).place(x=10,y=240)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=170,y=240)
    label=tkinter.Label(nx,text="Doctors Specialize :-",font=("arialbold",10,BOLD)).place(x=10,y=280)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=170,y=280)
    bt=Button(nx,text="UPDATE",fg="white",bg="black",font=("arialbold",10))
    bt.place(x=20,y=350)
    bt=Button(nx,text="DELETE",fg="white",bg="black",font=("arialbold",10))
    bt.place(x=250,y=350)
      
bt3=tkinter.Button(root,text="Doctors Details",fg="white",bg="black",font=("arialbold",30),command=next2)
bt3.place(x=20,y=400)

def next3():
    nx=Tk() 
    nx.title("Billing")
    nx.geometry("650x500+450+150")
    nx.maxsize(650,500)
    nx.minsize(650,500)
    lbl=Label(nx,text="BILLING",bd=20,relief=SUNKEN,fg="black",bg="white",font=("times new roman",20,BOLD)).pack()
    label=tkinter.Label(nx,text="Bed No. :-",font=("arialbold",10,BOLD)).place(x=10,y=80)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=140,y=80)
    label=tkinter.Label(nx,text="Patient Name :-",font=("arialbold",10,BOLD)).place(x=10,y=120)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=140,y=120)
    label=tkinter.Label(nx,text="Admit date :-",font=("arialbold",10,BOLD)).place(x=10,y=160)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=140,y=160)
    label=tkinter.Label(nx,text="Discharge Date :-",font=("arialbold",10,BOLD)).place(x=10,y=200)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=140,y=200)
    label=tkinter.Label(nx,text="Mobile No. :-",font=("arialbold",10,BOLD)).place(x=10,y=240)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=140,y=240)
    label=tkinter.Label(nx,text="Medicine :-",font=("arialbold",10,BOLD)).place(x=10,y=280)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=140,y=280)
    label=tkinter.Label(nx,text="Total Amount :-",font=("arialbold",10,BOLD)).place(x=10,y=320)
    entry1=Entry(nx,relief="sunken",bd=2)
    entry1.place(x=140,y=320)
    bt=Button(nx,text="UPDATE",fg="white",bg="black",font=("arialbold",10))
    bt.place(x=20,y=400)
    bt=Button(nx,text="DELETE",fg="white",bg="black",font=("arialbold",10))
    bt.place(x=250,y=400)
    
bt4=tkinter.Button(root,text="Billing",fg="white",bg="black",font=("arialbold",30),command=next3)
bt4.place(x=20,y=500)


root.mainloop()