
import mysql.connector as sql
conn=sql.connect(host='Localhost',user='root',password='Abhijeet652@',database='railways_management',port='3305')
if conn.is_connected():
 print('successfully connected')



print("<---------------------------------------->\n")
print("<--Railway Management System-->")
loop=True
while(loop):
    try:
        # print("Enter passenger name: ")
        # # print all possible passengers using mysql
        # # fetch_all_userData()
        # # take input for which want to do operartion 
        # id = int(input("\nEnter userID : \t"))
        # # print selected user 
        # fetch_selected_userData(id)              

        # want to insert or retrieve the data ?
        print("\nPress 1 to Create passengers ")
        print("Press 2 to update passengers ")
        print("Press 3 to delete passengers ")
        print("Press 4 to insert Train Details")
        print("Press 5 to update Train Details")
        print("Press 6 to delete Train Details")
        print("Press 7 to show all Passengers")
        print("Press 8 to show all train Detail")
        print("Press 9 to show PNR NO")

        op = int(input("Enter operartion to be performed from above :"))
        print("\n")

        # create train_details if not
        def create_train_details_ifNot(self):
            query='create table if not exists train_details(tid int auto_increment,tname varchar(100),tno int ,fare int,cls varchar(60),pnr_no int ,status varchar(50),primary key(tid))'
            cur=self.mydb.cursor()
            cur.execute(query)
    
        # create passengers if not
        def create_passengers_ifNot(self):
            query='create table if not exists todo(pid int auto_increment,pname varchar(100),age int,source varchr(50),destination varchar(50), primary key(pid))'
            cur=self.mydb.cursor()
            cur.execute(query)      

        if op == 1: # passengers insertion
            pname= input("Enter passenger name : ")
            age= input("Enter age : ")
            source= input("Enter source: ")
            destination= input("Enter destination : ")
            query="insert into passengers(pname,age,source,destination) values('{}',{},'{}','{}')".format(pname,age,source,destination)
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            print('Passenger added successfully !!!')

        if op == 2: #  update passengers 
            pid=int(input("Enter passenger id: "))    
            pname= input("Enter passenger name tobe updated : ")
            age= input("Enter age tobe updated : ")
            source= input("Enter source tobe updated: ")
            destination= input("Enter destination to be updated: ")
            query="update passengers set pname='{}',age={},source='{}',destination='{}' where pid = {} ".format(pname,age,source,destination,pid)
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            print('Passenger Updated successfully !!!')

        if op == 3: #  delete passengers 
            pid= input("Enter passenger id tobe deleted : ")
            pname= input("Enter passenger name tobe deleted : ")
            query="delete from passengers where pid = {} and pname='{}' ".format(pid,pname)
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            print('Passenger Deleted successfully !!!')

        if op == 4: # train details insertion
            tname= input("Enter train name : ")
            tno= input("Enter train number : ")
            fare= input("Enter fare : ")
            cls= input("Enter cls(Ac/Slp/General): ")
            pnr_no= input("Enter pnr_no: ")
            status= input("Enter status(Occupied/Available): ")  
            query="insert into train_details(tname,tno,fare,cls,pnr_no,status) values('{}',{},{},'{}',{},'{}')".format(tname,tno,fare,cls,pnr_no,status)
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            print('Train details added successfully !!!')

        if op == 5: # train details updation
            tname= input("Enter train name : ")
            tno= input("Enter train number : ")
            fare= input("Enter fare : ")
            cls= input("Enter cls(Ac/Slp/General): ")
            pnr_no= input("Enter pnr_no: ")
            status= input("Enter status(Occupied/Available): ")
            query="update train_details set tname='{}',tno={},fare={},cls='{}',pnr_no={},status='{}' where tname = {} ".format(tname,tno,fare,cls,pnr_no,status,tname)
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            print('Train details updated successfully !!!')

        if op == 6: # train details deletion
            tname= input("Enter train name : ")
            tno= input("Enter train number : ")  
            query="delete from train_details where tname = '{}' and tno='{}'".format(tname,tno)
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            print('Train details deleted successfully !!!')

        def fetch_passengers_Data():
            query="select * from passengers"
            cur=conn.cursor()
            cur.execute(query)
            for row in cur:
                print(f" '''\nPassengerID: {row[0]}\nPassengeName: {row[1]}\nage: {row[2]}\nsource: {row[3]}\ndestination: {row[4]}\n ''' ")  

        if op == 7: #fetch all passengers info
            fetch_passengers_Data()
            pass

        
        def fetch_train_details_Data():
            query="select * from train_details"
            cur=conn.cursor()
            cur.execute(query)
            for row in cur:
                print(f" '''\nTrainID: '{row[0]}'\ntname: '{row[1]}'\ntno: '{row[2]}'\nfare: '{row[3]}'\ncls: '{row[4]}'\npnr_no: '{row[5]}'\nstatus: '{row[6]}'\n ''' ")    

        if op == 8: #fetch all train details info
            fetch_train_details_Data()
            pass
                
        if op == 9: #Get Pnr_no by id
            tname= input("Enter train name : ")
            query="select pnr_no from train_details where tname='{}' ".format(tname)
            cur=conn.cursor()
            cur.execute(query)
            for row in cur:
                print(f"Pnr_number of entered '{tname}' train is '{row[0]}'. ") 

        print("---------------------------------------------")

    except Exception as e:
        print("Wrong Input !!!",e)
        print("---------------------------------------------")

# def create_passengers():
#        query= 'create table if not exits passengers(pname varchar(30),age varchar(25),trainno varchar(25),noofpassengers varchar(25),cls varchar(30),destination varchar(30),amount varchar(20),status varchar(25),PNR NO varchar(25))'
#        c1=conn.cursor()
#        c1.execute(query)
#        print('passenger table created')


# def add_passengers():
#     c1=conn.cursor()
#     L=[]
#     pname=input("ENTER NAME:")
#     L.append(pname)
#     age=input("ENTER AGE:")
#     L.append(age)
#     trainno=input("ENTER TRAIN NO:") 
#     L.append(trainno)
#     noofpassengers=input("ENTER NO OF PASSENGERS:")
#     L.append(noofpassengers)
#     cls=input("ENTER CLASS:")
#     L.append(cls)
#     destination=input("ENTER DESTINATION:")
#     L.append(destination)
#     amount=input("ENTER FARE:")
#     L.append(amount)
#     status=InterruptedError("ENTER STATUS:")
#     L.append(status)
#     PNRNO=input("ENTER PNRNO:")
#     L.append(PNRNO)
#     pas=(L)
#     sql="insert into passengers(pname,age,trainno,noofpassengers,cls,destination,amount,status,PNR NO)values(%s,%s,%s,%s,%s,%s.%s,%s,%s)"
#     c1.execute(sql,pas)
#     conn.commit()
#     print('Record Of Passengers Inserted')
#     df=sql("select*from passengers",conn)
#     print(df)


# def create_trainsdetail():
#     query='create table if not exits trainsdetail(tname varchar(30),tnum varchar(25),source varchar(30),destination varchar(30),fare varchar(20),general varchar(25),ac1 varchar(25),slp varchar (25)'
#     c1=conn.cursor()
#     c1.execute(query)
#     print('table tainsdetail created')

# def add_traindetail():
#     c1=conn.cursor()
#     df=("select*from traindetail",conn)
#     print(df)  
#     L=[]
#     tname=input("ENTER TRAIN NAME:")
#     L.append(tname)
#     tnum=input("ENTER TRAIN NUMBEER:")
#     L.append(tnum)
#     source=input("ENTER SOURCE OF TRAIN:")
#     L.append(source)
#     destination=input("ENTER DESTINATION OF TRAIN:")
#     L.append(destination)
#     fare=input("ENTER FARE OF TRAIN:")
#     L.append(fare)
#     general=("ENTER NO OF SEATS IN GENERAL:")
#     L.append(general)
#     ac1=("ENTER NO OF SEATS IN ac1:")
#     L.append(ac1)
#     slp=("ENTER NO OF SEATS IN slp:")
#     L.append(slp)
#     f=(L)
#     sql="insert into trainsdetails(tname,tnum,source,destination,fare,general,ac1,slp)values(%s,%s,%s,%s,%s,%s.%s,%s)"
#     c1.execute(sql,f)
#     conn.commit()
#     print('Record inserted in Trains Detail')



# def showtrainsdetail():
#     print('ALL TRAINS DETAIL')
#     df=sql("select*trainsdetail",conn) 
#     print(df)


# def showpassengers():
#     print('ALL PASSENGERS DETAIL')    
#     df=sql("select*from passengers",conn)
#     print(df)


# def disp_pnrno():
#     print("PNR STATUS WINDOW")  
#     a=(input("Enter Train no:"))  
#     qry="select pname,status from passengers where trainno=%s;"%(a,)   
#     df=sql(qry,conn)
#     print(df)

# opt=""
# opt=int(input("enter your choice:")) 
# if opt==1:
#    create_passengers
# elif opt==2:
#      add_passengers
# elif opt==3:
#      create_trainsdetail   
# elif opt==4:
#      add_traindetail   
# elif opt==5:
#      showtrainsdetail
# elif opt==6:
#      showpassengers   
# elif opt==7:   
#      disp_pnrno  
# else:
#     print('Invalid option')          