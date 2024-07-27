print("MAIN MENU")
print("Select operation.")
print("1.Number system converter")
print("2.Python Numeric data type converter")
print("3.Data type converter")
print("4.Graph plot")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        
#block1

        if choice == '1':
            print("Select the number system to convert")
            print("1.Binary")
            print("2.Octal")
            print("3.Decimal")
            print("4.Hexadecimal")
            print("5.Character to ASCII")

            while True:
                ch = input("Enter choice(1/2/3/4/5): ")
                import logger

                if ch in ('1', '2', '3', '4', '5'):
                    value =int(input("Enter value: "))

                    if ch == '1':
                        print("Decimal value: ", int(value))
                        print("Octal value: ", oct(value))
                        print("Hexadecimal value: ", hex(value))

                    elif ch == '2':
                        print("Binary value: ", bin(value))
                        print("Decimal value: ", int(value))
                        print("Hexadecimal value: ", hex(value))

                    elif ch == '3':
                        print("Binary value: ", bin(value))
                        print("Octal value: ", oct(value))
                        print("Hexadecimal value: ", hex(value))

                    elif ch == '4':
                        print("Binary value: ", bin(value))
                        print("Octal value: ", oct(value))
                        print("Decimal value: ", int(value))

                    elif ch == '5':
                        print("ASCII value: ", ord(str(value)))

                    lt = [["Binary value: ", bin(value)], ["Octal value: ", oct(value)],
                          ["Decimal value: ", int(value)],["Hexadecimal value: ", hex(value)],
                          ]


                    logger.log(lt)

                    break

                else:
                    print("Invalid Input")


#block2

        elif choice == '2':
            print("Select which Python number data type to convert.")
            print("1.Integer")
            print("2.Float")
            print("3.Complex")
            print("4.To a string")

            while True:
                ch1 = input("Enter choice(1/2/3/4): ")

                if ch1 in ('1', '2', '3', '4'):
                    num =(input("Enter value: "))
                    import logger

                    if ch1 == '1':
                        print("Float type:", float(num))
                        print("Complex type:", complex(num))
                        print("String type:", str(num))

                    elif ch1== '2':
                        print("Integer type:", int(num))
                        print("Complex type:", complex(num))
                        print("String type:", str(num))

                    elif ch1 == '3':
                        num = complex(num)
                        print("Integer type:", int(abs(num)))
                        print("Float type:", float(abs(num)))
                        print("String type:", str(abs(num)))

                    elif ch1 == '4':
                        print("Integer type:", int(num))
                        print("Float type:", float(num))
                        print("Complex type:", complex(num))

                    lt = [["Integer type:", int(abs(num))] ,["Float type:", float(abs(num))] , ["String type:", str(abs(num))] ,
                          ["Complex type:", complex(num)]]
                    logger.log(lt)

                    break

                else:
                    print("Invalid Input")

                break

#block3

        elif choice == '3':
            print("Select the Data type to convert")
            print("1.String")
            print("2.List")
            print("3.Tuple")
            print("4.Set")
                  
            while True:
                ch3 = input("Enter choice(1/2/3/4): ")
                import logger

                if ch3 in ('1', '2', '3', '4', '5'):
                    data =(input("Enter value: "))

                    if ch3 == '1':
                        print("List: ", list(data))
                        print("Tuple: ", tuple(data))
                        print("Set: ", set(data))

                    elif ch3 == '2':
                       print("String: ", str(data))
                       print("Tuple: ", tuple(data))
                       print("Set: ", set(data))

                    elif ch3 == '3':
                       print("String: ", str(data))
                       print("List: ", list(data))
                       print("Set: ", set(data))

                    elif ch3 == '4':
                       print("String: ", str(data))
                       print("List: ", list(data))
                       print("Tuple: ",tuple(data))

                    lt =  [["List: ", list(data)] , ["Tuple: ", tuple(data)] , ["String: ", str(data)] , ["Set: ", set(data)]]
                    logger.log(lt)

                    break

                
                else:
                    print("Invalid Input")

#block4

        if choice == '4':
            
            import matplotlib.pyplot as plt

            x = list(input("Enter X co-ordinates separated with comma : "))
            y = list(input("Enter Y co-ordinates separated with comma : "))

            plt.plot(x, y, color = 'c', marker = 'h')

            plt.xlabel('x - axis')
            plt.ylabel('y - axis')
             
            plt.title('Required Graph')
            plt.show()


    break

import logger
logger.show()

















            


































            


