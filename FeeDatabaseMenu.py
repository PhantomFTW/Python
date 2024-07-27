import operations


print("\n------------------WELCOME TO THE FEE logger------------------\n")

def menuset(): 
    print("Enter 1 : To Add Student")
    print("Enter 2 : To View Student ")
    print("Enter 3 : To Deposit Fee ")
    print("Enter 4 : To Remove Student")
    print("Enter 5 : To View Fee of Any Student")

    userInput = int(input("Please Select An Above Option: ")) 
    if(userInput == 1):
        operations.studentinsert()
    elif (userInput==2):
        operations.studentdesc()
    elif (userInput==3):
        operations.feedeposit()
    elif (userInput==4):
        operations.removestudent()
    elif (userInput==5):
        operations.feedesc()
    else:
        print("Enter correct choice. . .  ")

    runagain()
    


def runagain():
    runagn = input("\nRun again? y/n: ")
    if(runagn.lower() == 'y'):
        menuset()
    
        
menuset()


