import math
import keyword

def variable_address():
    x = 99
    print("Address of variable x is:", id(x))
    y = int(input("Enter a number: "))
    print("Address of variable y is:", id(y))

def area_perimeter_shapes():
    l = float(input("Enter length for rectangle: "))
    b = float(input("Enter breadth for rectangle: "))
    s = float(input("Enter side for square: "))
    base = float(input("Enter base for triangle: "))
    height = float(input("Enter height for triangle: "))
    s1 = float(input("Enter side 1 for triangle: "))
    s2 = float(input("Enter side 2 for triangle: "))
    s3 = float(input("Enter side 3 for triangle: "))
    r = float(input("Enter radius for circle: "))

    area1 = l * b
    peri1 = 2 * (l + b)
    area2 = s * s
    peri2 = 4 * s
    area3 = 0.5 * base * height
    peri3 = s1 + s2 + s3
    area4 = 3.14 * r * r
    peri4 = 2 * 3.14 * r

    print("Area of rectangle =", area1)
    print("Perimeter of rectangle =", peri1)
    print("Area of square =", area2)
    print("Perimeter of square =", peri2)
    print("Area of triangle =", area3)
    print("Perimeter of triangle =", peri3)
    print("Area of circle =", area4)
    print("Perimeter of circle =", peri4)

def arithmetic_operations():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Original value of a =", a)
    print("Original value of b =", b)

    print("value after using + operator is", a + b)
    print("value after using - operator is", a - b)
    print("value after using * operator is", a * b)
    print("value after using / operator is", a / b)
    print("value after using // operator is", a // b)
    print("value after using ** operator is", a ** b)
    print("value after using % operator is", a % b)

def assignment_operations():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Original value of a =", a)
    print("Original value of b =", b)

    a += b
    print("value of a after using += operator is", a)
    a -= b
    print("value of a after using -= operator is", a)
    a *= b
    print("value of a after using *= operator is", a)
    a /= b
    print("value of a after using /= operator is", a)
    a //= b
    print("value of a after using //= operator is", a)
    a **= b
    print("value of a after using **= operator is", a)
    a %= b
    print("value of a after using %= operator is", a)

def average_percentage():
    m1 = float(input("Enter marks in English: "))
    m2 = float(input("Enter marks in Physics: "))
    m3 = float(input("Enter marks in Chemistry: "))
    m4 = float(input("Enter marks in Mathematics: "))
    m5 = float(input("Enter marks in Computer Science: "))
    total = m1 + m2 + m3 + m4 + m5
    avg = total / 5
    per = (total / 500) * 100
    print("Total marks =", total)
    print("Average marks =", avg)
    print("Percentage =", per, "%")

def digit_check():
    num = int(input("Enter a number: "))

    if 9 < num < 100:
        print("Two digit number")
    elif 99 < num < 1000:
        print("Three digit number")
    elif 999 < num < 10000:
        print("Four digit number")
    else:
        print("Number is <= 9 or >= 10000")

def circle_calculations():
    def area(r):
        return 3.14 * r * r

    def perimeter(r):
        return 2 * 3.14 * r

    radius = int(input("Enter radius: "))
    ans1 = area(radius)
    ans2 = perimeter(radius)

    print("Area of circle =", ans1)
    print("Perimeter of circle =", ans2)

def complex_operations():
    n1 = complex(input("Enter the first complex number in the form of a+bj: "))
    n2 = complex(input("Enter the second complex number in the form of a+bj: "))
    print("Sum =", n1 + n2)
    print("Difference =", n1 - n2)
    print('Product =', n1 * n2)

def complex_parts():
    x = 2 + 9j
    y = -6 - 7j
    print("Complex number is:", x)
    print("Real part is:", x.real)
    print("Imaginary part is", x.imag)
    print("Complex number is:", y)
    print("Real part is:", y.real)
    print("Imaginary part is", y.imag)

def distance_calculation():
    s = float(input("Enter speed: "))
    t = float(input("Enter time: "))
    d = s * t
    print("Distance covered =", d)

def conversion_feet_inches_km_meters():
    def convert1(f):
        return f * 12.0

    def convert2(k):
        return k * 1000

    ft = float(input("Enter distance in feet: "))
    inc = convert1(ft)
    print("Distance in feet:", ft)
    print("Distance in inches:", inc)

    kms = float(input("Enter distance in kilometres: "))
    mtrs = convert2(kms)
    print("Distance in kilometre:", kms)
    print("Distance in metres:", mtrs)

def rectangle_calculations():
    def area(l, b):
        return l * b

    def perimeter(l, b):
        return 2 * (l + b)

    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    ans1 = area(length, breadth)
    ans2 = perimeter(length, breadth)

    print("Area of rectangle =", ans1)
    print("Perimeter of rectangle =", ans2)

def shape_area_functions():
    def arearect(l, b):
        a = l * b
        print("Area is:", a)

    def areacircle(r):
        a = 3.14 * r * r
        print("Area is:", a)

    def areatri(base, ht):
        a = 0.5 * base * ht
        print("Area is:", a)

    l1 = float(input("Enter length: "))
    b1 = float(input("Enter breadth: "))
    arearect(l1, b1)

    rad = float(input("Enter radius: "))
    areacircle(rad)

    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    areatri(base, height)

def area_perimeter_functions():
    def rect(l, b):
        a = l * b
        p = 2 * (l + b)
        print("Area of rectangle is:", a)
        print("Perimeter of rectangle is:", p)

    def square(s):
        a = s * s
        p = 4 * s
        print("Area of square is:", a)
        print("Perimeter of square is:", p)

    def circle(r):
        a = 3.14 * r * r
        p = 2 * 3.14 * r
        print("Area of circle is:", a)
        print("Perimeter of circle is:", p)

    l1 = float(input("Enter length of rectangle: "))
    b1 = float(input("Enter breadth of rectangle: "))
    rect(l1, b1)

    side = float(input("Enter side: "))
    square(side)

    radius = float(input("Enter radius: "))
    circle(radius)

def person_info():
    def person(name, age):
        print("Name of person is:", name)
        print("Age of person is:", age)

    nm = input("Enter name of person: ")
    a = int(input("Enter age of person: "))
    person(nm, a)

def check_identity():
    a = 34
    b = 34
    if a is b:
        print('Both a and b have the same identity')
    else:
        print('a and b have different identities')

    b = 99
    if a is not b:
        print('a and b have different identities')
    else:
        print('a and b have the same identity')

def print_keywords():
    print("All keywords in Python are:")
    print(keyword.kwlist)

def logical_operators():
    a = 60
    b = 80
    c = 40
    d = 100

    if a > b and b > c:
        print("a is the greatest")
    if a > b or b > c:
        print("hello")
    if c > a and c > d:
        print("c is the greatest")
    if not a > b:
        print("b is greater")

def bitwise_operators():
    a = 2
    b = 3

    print("value of a & b:", a & b)
    print("value of a | b:", a | b)
    print("value of ~a:", ~a)
    print("value of a ^ b:", a ^ b)
    print("value of a >> 2:", a >> 2)
    print("value of a << 2:", a << 2)

def maximum_minimum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a > b and a > c:
        print("Maximum value is", a)
    elif b > a and b > c:
        print("Maximum value is", b)
    else:
        print("Maximum value is", c)

    if a < b and a < c:
        print("Minimum value is", a)
    elif b < a and b < c:
        print("Minimum value is", b)
    else:
        print("Minimum value is", c)

def check_vowel():
    ch = input("Enter any character: ")

    if ch in ('a', 'e', 'i', 'o', 'u'):
        print("It is a Vowel")
    else:
        print("It is a Consonant")

def sum_digits():
    num = int(input("Enter a number: "))
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    print("Sum of digits is:", sum)

def triangle_calculations():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))

    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

def swap_numbers():
    def swap(x, y):
        x, y = y, x
        return x, y

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Before swap x =", x, " y =", y)
    x, y = swap(x, y)
    print("After swap x =", x, " y =", y)

def print_pattern():
    rows = int(input("Enter number of rows: "))

    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print("\n")

def check_positivity():
    num = int(input("Enter a number: "))

    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")

def circle_operations():
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r

    print("Area of circle =", area)
    print("Circumference of circle =", circumference)

def temperature_conversion():
    choice = input("Choose (C) for Celsius to Fahrenheit or (F) for Fahrenheit to Celsius: ").upper()
    if choice == 'C':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C is {f}°F")
    elif choice == 'F':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F is {c}°C")
    else:
        print("Invalid choice")

def main_menu():
    options = {
        1: variable_address,
        2: area_perimeter_shapes,
        3: arithmetic_operations,
        4: assignment_operations,
        5: average_percentage,
        6: digit_check,
        7: circle_calculations,
        8: complex_operations,
        9: complex_parts,
        10: distance_calculation,
        11: conversion_feet_inches_km_meters,
        12: rectangle_calculations,
        13: shape_area_functions,
        14: area_perimeter_functions,
        15: person_info,
        16: check_identity,
        17: print_keywords,
        18: logical_operators,
        19: bitwise_operators,
        20: maximum_minimum,
        21: check_vowel,
        22: sum_digits,
        23: triangle_calculations,
        24: swap_numbers,
        25: print_pattern,
        26: check_positivity,
        27: circle_operations,
        28: temperature_conversion,
        29: exit
    }

    while True:
        print("\nMain Menu")
        print("1. Variable Address")
        print("2. Area and Perimeter of Shapes")
        print("3. Arithmetic Operations")
        print("4. Assignment Operations")
        print("5. Average and Percentage")
        print("6. Digit Check")
        print("7. Circle Calculations")
        print("8. Complex Operations")
        print("9. Complex Parts")
        print("10. Distance Calculation")
        print("11. Conversion between Feet-Inches and KM-Meters")
        print("12. Rectangle Calculations")
        print("13. Shape Area Functions")
        print("14. Area and Perimeter Functions")
        print("15. Person Info")
        print("16. Check Identity")
        print("17. Print Keywords")
        print("18. Logical Operators")
        print("19. Bitwise Operators")
        print("20. Maximum and Minimum")
        print("21. Check Vowel")
        print("22. Sum of Digits")
        print("23. Triangle Calculations")
        print("24. Swap Numbers")
        print("25. Print Pattern")
        print("26. Check Positivity")
        print("27. Circle Operations")
        print("28. Temperature Conversion")
        print("29. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice in options:
                options[choice]()
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main_menu()
