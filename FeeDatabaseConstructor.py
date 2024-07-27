import mysql.connector


mydb = mysql.connector.connect(host='localhost',
                             user='root',
                             passwd='arnav',
                             database='student')
mycursor=mydb.cursor()

def studentinsert():
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    name=input("Enter the Name: ")
    L.append(name)
    age=int(input("Enter Age of Student : "))
    L.append(age)
    classs=input("Enter the Class : ")
    L.append(classs)
    city=input("Enter the City ofthe Student : ")
    L.append(city)
    student=(L)
    sql="insert into student (roll,name,age,class,city) values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,student)
    mydb.commit()
    print("record added succesfully")

def studentdesc():
    print("Select the search criteria : ")
    print("1. Roll")
    print("2. Name")
    print("3. Age")
    print("4. City")
    print("5. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
        s=int(input("Enter roll no : "))
        rl=(s,)
        sql="select * from student where roll=%s"
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input("Enter Name : ")
        rl=(s,)
        sql="select * from student where name=%s"
        mycursor.execute(sql,rl)
    elif ch==3:
        s=int(input("Enter age : "))
        rl=(s,)
        sql="select * from student where age=%s"
        mycursor.execute(sql,rl)
    elif ch==4:
        s=input("Enter City : ")
        rl=(s,)
        sql="select * from student where City=%s"
        mycursor.execute(sql,rl)
    elif ch==5:
        sql="select * from student"
        mycursor.execute(sql)
        
    res=mycursor.fetchall()
    print("The Students details are as follows : ")
    print("(ROll, Name, Age, Class, City)")
    for x in res:
        print(x)
        
def feedeposit():
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    feedeposit=int(input("Enter the Fee to be deposited : "))
    L.append(feedeposit)
    month=input("Enter month of fee : ")
    L.append(month)
    fee=(L)
    sql="insert into fee (roll,feeDeposit,Month) values (%s,%s,%s)"
    mycursor.execute(sql,fee)
    mydb.commit()

def feedesc():
    print("Please enter the details to view the fee details :")
    roll=int(input("Enter the roll number of the student whose fee is to be viewed : "))
    sql="Select Student.Roll, Student.Name, Student.Class, sum(fee.feeDeposit), fee.month from Student INNER JOIN fee ON Student.roll=fee.roll and fee.roll = %s"
    rl=(roll,)
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    for x in res:
        print(x)
    
    
def removestudent():
    roll=int(input("Enter the roll number of the student to be deleted : "))
    rl=(roll,)
    sql="Delete from fee where roll=%s"
    mycursor.execute(sql,rl)
    sql="Delete from Student where roll=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
    
