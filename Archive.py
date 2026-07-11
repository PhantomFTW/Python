# ==========================================
# IMPORTS
# ==========================================
import math
import matplotlib.pyplot as plt

# ==========================================
# DATA STRUCTURES 
# ==========================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def add(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def traverse(self):
        current = self.head
        while current != None:
            print(current.data) 
            current = current.next

# ==========================================
# UTILITY FUNCTIONS 
# ==========================================
def gcd(a, b):
    l = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            l.append(i)
    return l[-1]

def square(x):
    y = x * x
    return y

def squaremod(x):
    y = x * x
    print(y)
    return y

def average(a, b):
    c = (a + b) / 2
    return c

def average3(a, b, c):
    return (a + b + c) / 3

def custom_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def inrange(x, a, b):
    return x >= a and x <= b

def belongs(v, l):
    for x in l:
        if x == v:
            return True
    return False

def locatepos(v, l):
    pos = 0
    for x in l:
        if x == v:
            return pos
        pos += 1
    return -1

# ==========================================
# MAIN INTERACTIVE MENU
# ==========================================
if __name__ == "__main__":
    print("MAIN MENU")
    print("Select operation.")
    print("1. Number system converter")
    print("2. Python Numeric data type converter")
    print("3. Data Type Converter")
    print("4. Plot Graph")
    print("5. Calculate Weekly Average Temperature")

    while True:
        choice = input("\nEnter choice(1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4', '5'):
            
            # --- BLOCK 1: Number System Converter ---
            if choice == '1':
                print("Select the number system to convert")
                print("1. Binary")
                print("2. Octal")
                print("3. Decimal")
                print("4. Hexadecimal")
                print("5. Character to ASCII")

                while True:
                    ch = input("Enter choice(1/2/3/4/5): ")

                    if ch in ('1', '2', '3', '4', '5'):
                        value = int(input("Enter value: "))

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
                            print("ASCII value: ", ord(value))
                        break
                    else:
                        print("Invalid Input. Try again.")
                        
            # --- BLOCK 2: Numeric Data Type Converter ---
            elif choice == '2':
                print("Select which Python number data type to convert.")
                print("1. Integer")
                print("2. Float")
                print("3. Complex")
                print("4. To a string")

                while True:
                    ch1 = input("Enter choice(1/2/3/4): ")

                    if ch1 in ('1', '2', '3', '4'):
                        num = input("Enter value: ")

                        if ch1 == '1':
                            print("Float type:", float(num))
                            print("Complex type:", complex(num))
                            print("String type:", str(num))
                        elif ch1 == '2':
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
                        break
                    else:
                        print("Invalid Input. Try again.")

            # --- BLOCK 3: Iterable Data Type Converter ---
            elif choice == '3':
                print("Select the Data type to convert")
                print("1. String")
                print("2. List")
                print("3. Tuple")
                print("4. Set")
                      
                while True:
                    ch3 = input("Enter choice(1/2/3/4): ")

                    if ch3 in ('1', '2', '3', '4'):
                        data = input("Enter value: ")

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
                           print("Tuple: ", tuple(data))
                        break
                    else:
                        print("Invalid Input. Try again.")

            # --- BLOCK 4: Plot Graph ---
            elif choice == '4':
                x_input = input("Enter X co-ordinates separated with comma: ")
                y_input = input("Enter Y co-ordinates separated with comma: ")
                
                x = [float(i) for i in x_input.split(',')]
                y = [float(i) for i in y_input.split(',')]

                plt.plot(x, y, color='c', marker='h')
                plt.xlabel('x - axis')
                plt.ylabel('y - axis')
                plt.title('Required Graph')
                plt.show()
                
            # --- BLOCK 5: Weekly Average Temperature ---
            elif choice == '5':
                print("\n--- Weekly Average Temperature Calculator ---")
                a1 = float(input("Enter Temperature on Monday: "))
                a2 = float(input("Enter Temperature on Tuesday: "))
                a3 = float(input("Enter Temperature on Wednesday: "))
                a4 = float(input("Enter Temperature on Thursday: "))
                a5 = float(input("Enter Temperature on Friday: "))
                a6 = float(input("Enter Temperature on Saturday: "))
                a7 = float(input("Enter Temperature on Sunday: "))

                avg = (a1 + a2 + a3 + a4 + a5 + a6 + a7) / 7
                print(f"Average Temperature = {avg:.2f}")

        else:
            print("Invalid Input. Please select from 1-5.")