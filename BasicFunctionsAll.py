def average_temperature():
    # Collects temperatures for a week and calculates the average
    a1 = float(input("Enter Temperature on Monday: "))
    a2 = float(input("Enter Temperature on Tuesday: "))
    a3 = float(input("Enter Temperature on Wednesday: "))
    a4 = float(input("Enter Temperature on Thursday: "))
    a5 = float(input("Enter Temperature on Friday: "))
    a6 = float(input("Enter Temperature on Saturday: "))
    a7 = float(input("Enter Temperature on Sunday: "))

    avg = (a1 + a2 + a3 + a4 + a5 + a6 + a7) / 7
    print("Average Temperature =", avg)

def simple_calculator():
    # Performs basic arithmetic operations
    a = int(input("Enter First number : "))
    b = int(input("Enter Second number : "))
    c = input("Enter Any ONE of the Operator +,-,*,/ :  ")
    if c == '+':
        print("The Result is : ", a + b)
    elif c == '-':
        print("The Result is : ", a - b)
    elif c == '*':
        print("The Result is : ", a * b)
    elif c == '/':
        print("The Result is : ", a / b)
    elif c == '%':
        print("The result is :", a % b)
    else:
        print("Wrong Operator Entered")

def calculate_grade():
    # Calculates the grade based on average marks of 5 subjects
    s1 = float(input("Enter marks of the first subject: "))
    s2 = float(input("Enter marks of the second subject: "))
    s3 = float(input("Enter marks of the third subject: "))
    s4 = float(input("Enter marks of the fourth subject: "))
    s5 = float(input("Enter marks of the fifth subject: "))
    avg = (s1 + s2 + s3 + s4 + s5) / 5

    if avg >= 85:
        print("Grade: A")
    elif 75 <= avg < 85:
        print("Grade: B")
    elif 65 <= avg < 75:
        print("Grade: C")
    elif 55 <= avg < 65:
        print("Grade: D")
    elif 45 <= avg < 50:
        print("Grade: E")
    else:
        print("Grade: F")

def check_leap_year():
    # Checks if a given year is a leap year
    year = int(input("Enter Year: "))
    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year")
    elif year % 100 == 0:
        print(year, "is not a Leap Year")
    elif year % 400 == 0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")

def find_largest_number():
    # Finds the largest number among three numbers
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    n3 = float(input("Enter third number: "))

    if n1 >= n2 and n1 >= n3:
        largest = n1
    elif n2 >= n1 and n2 >= n3:
        largest = n2
    else:
        largest = n3

    print("The largest number is", largest)

def solve_quadratic():
    # Solves a quadratic equation
    import cmath
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    c = int(input('Enter third number: '))
    d = (b**2) - (4*a*c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The solutions are {0} and {1}'.format(sol1, sol2))

def print_numbers_while():
    # Prints numbers from -20 to 10 using a while loop
    i = -20
    while i < 11:
        print(i)
        i = i + 1

def print_numbers_for():
    # Prints numbers from 15 to -10 using a for loop
    for j in range(15, -11, -1):
        print(j)

def sum_and_product_of_n_terms():
    # Calculates the sum and product of first n terms
    n = int(input("Enter number of terms "))

    s = 0
    p = 1

    if n <= 0:
        print("Enter a whole positive number!")
    else:
        while n > 0:
            s = s + n
            p = p * n
            n = n - 1

    print("Sum of n terms is: ", s)
    print("Product of n terms is: ", p)

def even_odd_numbers_in_range():
    # Separates and prints even and odd numbers within a range
    a = int(input("Enter the start of range: "))
    b = int(input("Enter the end of range: "))

    n1 = []
    n2 = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            n1.append(i)
        else:
            n2.append(i)

    print("Even numbers:", n1)
    print("Odd numbers:", n2)

def print_multiplication_table():
    # Prints the multiplication table of a given number up to 10
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        m = i * n
        print(m)

def fibonacci_sequence():
    # Prints the Fibonacci sequence up to N terms
    N = int(input("How many terms? "))
    N1, N2 = 0, 1
    c = 0

    if N <= 0:
        print("Please enter a positive integer")
    elif N == 1:
        print("Fibonacci sequence up to", N, ":")
        print(N1)
    else:
        print("Fibonacci sequence:")
        while c < N:
            print(N1)
            Nth = N1 + N2
            N1 = N2
            N2 = Nth
            c += 1

def factorial_of_number():
    # Calculates the factorial of a given number
    n = int(input("Enter a number: "))
    f = 1
    if n < 0:
        print("Please enter a positive number")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, n + 1):
            f = f * i
        print("The factorial of", n, "is", f)

def factorial_sum_series():
    # Calculates a series sum using factorials
    import math
    def factorial(x):
        product = 1
        for i in range(1, x + 1):
            product *= i
        return product

    n = int(input("Enter the value of n: "))
    x = int(input("Enter the value of x: "))
    sum = 1
    for i in range(1, n):
        if i % 2 == 1:
            b = math.pow(x, i)
            sum -= b / factorial(i + 1)
        else:
            b = math.pow(x, i)
            sum += b / factorial(i + 1)
    print(sum)

def check_prime_number():
    # Checks if a given number is prime
    n = int(input("Enter a number: "))
    m = False
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                m = True
    if m:
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")

def check_palindrome():
    # Checks if a given number is a palindrome
    n = int(input("Enter number: "))
    orig = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if orig == rev:
        print("The number", orig, "is a palindrome.")
    else:
        print("The number", orig, "isn't a palindrome.")

def sum_of_digits():
    # Calculates the sum of the digits of a given number
    n = int(input("Please enter a number : "))
    s = 0
    while n > 0:
        r = n % 10
        s = s + r
        n = n // 10
    print("Sum of the digits of given number:", s)

def decimal_binary_conversion():
    # Converts a decimal number to binary and vice versa
    print("For Decimal to Binary Enter 1.")
    print("For Binary to Decimal Enter 2")
    x = int(input("Enter your choice: "))
    if x == 1:
        a = 1
        b = 0
        n1 = int(input("Enter a decimal number  "))
        while n1 > 0:
            r = int(n1 % 2)
            b = b + (a * r)
            n1 = int(n1 / 2)
            a = a * 10
        print("The binary value of the given number is ", b, '.')
    if x == 2:
        def bin(n):
            n2, d, c = n, 0, 1
            t = n2
            while t:
                dig = t % 10
                t = int(t / 10)
                d += dig * c
                c = c * 2
            return d

        n2 = int(input('Enter a binary number: '))
        print('The decimal value of the given number is =', bin(n2))

def area_of_shapes():
    # Calculates the area of different shapes
    def circ(r):
        area = 3.14 * r * r
        print('Area of circle =', area)

    def rect(l, b):
        area = l * b
        print('Area of rectangle =', area)

    def tri(a, b, c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
        print('Area of triangle =', area)

    def menu():
        n = int(input('Enter the value of option chosen: '))
        if n == 1:
            r = float(input("Enter the radius of the circle: "))
            circ(r)
        elif n == 2:
            a = float(input("Enter the length of first side of triangle: "))
            b = float(input("Enter the length of second side of triangle: "))
            c = float(input("Enter the length of third side of triangle: "))
            tri(a, b, c)
        elif n == 3:
            l = float(input("Enter the length of rectangle: "))
            b = float(input("Enter the breadth of rectangle: "))
            rect(l, b)
        else:
            print("Error: Please input a valid option.")
            menu()

    print('Menu:- \n1)Circle \n2)Triangle \n3)Rectangle')
    menu()

def print_patterns():
    # Prints various patterns
    rows = 6  # part i
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end="")
        print("\r")

    rows = 5  # part ii
    for i in range(rows, -1, -1):
        for j in range(0, i):
            print("#", end="")
        print("\r")

    num = "8642"  # part iii
    for i in range(4):
        print(num[:i + 1])

    n = 8  # part iv
    for a in range(n, 0, -1):
        for bc in range(1, n + 1 - a):
            print(" ", end='')
        for num in range(1, a + 1):
            print("$ ", end='')
        print('')

    n = 5  # part v
    for a in range(1, n + 1):
        for num in range(1, a + 1):
            print(num, end='')
        print('')

    n = 6  # part vi
    i = 0
    while i <= n - 1:
        j = 0
        while j < i:
            # display space
            print('', end=' ')
            j += 1
        k = i
        while k <= n - 1:
            print('&', end=' ')
            k += 1
        print()
        i += 1

    i = n - 1
    while i >= 0:
        j = 0
        while j < i:
            print('', end=' ')
            j += 1
        k = i
        while k <= n - 1:
            print('&', end=' ')
            k += 1
        print('')
        i -= 1

def string_character_analysis():
    # Analyzes and counts different types of characters in a string
    n = input("Enter a string: ")
    upper, lower, number, special, alpha = 0, 0, 0, 0, 0

    for i in n:
        if i.isalpha():
            alpha += 1
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i.isdigit():
            number += 1
        else:
            special += 1

    print('Alphabets:', alpha)
    print('Upper case letters:', upper)
    print('Lower case letters:', lower)
    print('Number:', number)
    print('Special characters:', special)

def word_count_in_string():
    # Counts the number of words and a specific substring in a string
    str = input("Enter the string: ")
    h = str.split()
    count = 0
    for i in h:
        count += 1

    print("The string has", count, "words")
    substr = input("Enter the substring you want to count: ")
    print(substr, "comes", str.count(substr), "times in the string")

def vowel_and_consonant_count():
    # Counts vowels and consonants in a string and swaps case
    str = input("Enter the string: ")
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    countv = 0
    final = ""
    countcon = 0

    for i in str:
        if i.isalpha():
            if i in vowels:
                countv += 1
            else:
                countcon += 1
                final += i
        else:
            final += i

    final = final.swapcase()
    print("The string has", countv, "vowels and", countcon, "consonants.")
    print("Final result:-\n", final)

def vowel_count_in_string():
    # Counts the number of vowels in a string
    str = input("Enter desired string: ")
    vowels = ['a', 'A', 'e', 'E', 'i', 'o', 'u', 'I', 'O', 'U']
    count = 0
    for a in str:
        if a in vowels:
            count += 1
        else:
            pass
    print('There are', count, 'vowels in the entered string.')

def string_length():
    # Calculates the length of a given string
    str = input("Enter the string: ")
    count = 0

    for i in str:
        count += 1

    print("The length of the entered string is:", count)

def convertbinoct (num,base=2):
    str1= " "
    while  num   !=0 :
         str1= str1+ str(num%base)
         num= num//base
       
    str1=  str1[ : :-1]
    print(str1)

