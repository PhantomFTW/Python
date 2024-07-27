c = 82
print(c)

a = 38 + 53
b = a + c
c = c + 1

print(a, b, c)

height = 1.85
height = 2 * height
print(height)

print(type(7), type(3.5))

height = 1.85
height = 2 * height
print(type(height))

print(a, b, c)

print(a < 100)
print(a < 100 and b < 150)
print(a < 100 or b < 150)
print(a < 100 or b > 150)
print(a < 100 and b > 150)
print(not (c > 100))

mylist = [1, 3.5, True]
print(mylist)

print(mylist[1])
mylist[1] = 92
print(mylist[1])
print(mylist)

# This line will raise an IndexError because mylist only has indices 0, 1, and 2.
# mylist[3] = False

print(len(mylist))
print(mylist[-1])
print(mylist[2], mylist[-2])
print(mylist[-3])

import math

def gcd(a, b):
    l = []

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            l.append(i)
    return l[-1]

print(gcd(700, 10))

print(7 + 2.5)
print(7 * 3.0)
print(7 / 3, 7 // 3, 7 % 3)
print(7.0 // 3.0)
print(2 ** 3)

import math
print(math.log(7), math.sqrt(2))

from math import *
print(sin(pi / 2), log(e))

import math as mt
print(mt.tan(mt.pi / 4))

mt.pi = 3
print(mt.pi)

m = 2 ** 83
n = 3 ** 158
p = m * n
print(m, n, p)

x = 7
y = False
z = True
print(x and y, x and True)
x = 7
y = 5
print(x and y, not (x and y))

print(False * x)