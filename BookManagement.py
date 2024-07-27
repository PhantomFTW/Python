

import mysql.connector as a

con = a.connect(host='localhost', user='root', passwd='root', database='library')

def addbook():
    name = input("Enter book name: ")
    code = input("Enter book code: ")
    total = input("Total books: ")
    sub = input("Enter subject: ")
    sql = 'INSERT INTO book VALUES (%s, %s, %s, %s)'
    data = (name, code, total, sub)
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data entered successfully")
    main()

def issueb():
    n = input("Enter name: ")
    r = input("Enter registration no: ")
    co = input("Enter book code: ")
    d = input("Enter date: ")
    a = "INSERT INTO issue VALUES (%s, %s, %s, %s)"
    data = (n, r, co, d)
    c = con.cursor()
    c.execute(a, data)
    con.commit()
    print("." * 10, "Data entered successfully")
    print("Book issued to:", n)
    bookup(co, -1)

def submitb():
    n = input("Enter name: ")
    r = input("Enter reg no: ")
    co = input("Enter book code: ")
    d = input("Enter date: ")
    a = "INSERT INTO submit VALUES (%s, %s, %s, %s)"
    data = (n, r, co, d)
    c = con.cursor()
    c.execute(a, data)
    con.commit()
    print("-" * 10, "Book submitted from:", n)
    bookup(co, 1)

def bookup(co, u):
    a = "SELECT total FROM book WHERE code=%s"
    data = (co,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "UPDATE book SET total=%s WHERE code=%s"
    d = (t, co)
    c.execute(sql, d)
    con.commit()
    main()

def dbook():
    ac = input("Enter book code: ")
    a = "DELETE FROM book WHERE code=%s"
    data = (ac,)
    c = con.cursor()
    c.execute(a, data)
    con.commit()
    print("-" * 10, "Book deleted from library")
    main()

def main():
    print("MANAGEMENT")
    print("1. ADD BOOK")
    print("2. ISSUE BOOK")
    print("3. SUBMIT BOOK")
    print("4. DELETE BOOK")
    print("5. EXIT")
    choice = input("Enter task no: ")
    
    if choice == '1':
        addbook()
    elif choice == '2':
        issueb()
    elif choice == '3':
        submitb()
    elif choice == '4':
        dbook()
    elif choice == '5':
        con.close()
        print("Exiting...")
    else:
        print("Wrong choice")
        main()

main()

