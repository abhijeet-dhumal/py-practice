students={1:"Harry",2:"Abhijeet",3:"Akshay"}
operation={1:"Add",2:"Delete",3:"Retrive"}
def getdate():
    import datetime
    return datetime.datetime.now()
print("School Management System")
try:
    print("Select client name:", end=" ")
    for key,value in students.items(): 
        print(f"Press {key} for {value} :")
    num=int(input())
    print(f"Selected student name is :{students[num]}")
    x='y'
    if x=='y':
        print("Enter operation to be performed :")
        for key,value in operation.items():
            print(f"Press {key} for {value}")
        opt=int(input())
        print(f"Selected oeration is :{operation[opt]}") 
        if opt is 1:
            name=str(input("Enter Student name:"))
            with open("student_data.txt","a") as op:
                op.write(f"[ {+} {str(getdate())} {+} ] {+} : {+} {4[name]}")
            op.close()

except exception as e:
    print(e)