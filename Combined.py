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

x = 5
print(type(x))

x = False
print(type(x))

def square(x):
    y = x * x
    return y

print(square(7))

a = square(7) + 32 + square(71)
print(a)

y = 377

print(square(8))
print(y)

def squaremod(x):
    y = x * x
    print(y)

squaremod(7)

#a = squaremod(7) + 32 + squaremod(73)
print(a)

def squaremod2(x):
    y = x * x
    print(y)
    return y

squaremod2(9)

#a = squaremod2(7) + 32 + squaremod2(73)
print(a)

def average(a, b):
    c = (a + b) / 2
    return c

print(average(3.7, 8.55))

def average3(a, b, c):
    return (a + b + c) / 3

print(average3(7, 9, 11))

def abs(x):
    y = x
    if x < 0:
        y = -x
    return y

print(abs(8), abs(-73))

def abs2(x):
    y = x
    if x >= 0:
        y = x
    else:
        y = -x
    return y

def abs(x):
    y = x
    if x >= 0:
        return x
    else:
        return -x

def inrange(x, a, b):
    if x >= a and x <= b:
        return True
    else:
        return False

print(inrange(3, 2, 4), inrange(2, 3, 4))

def inrange2(x, a, b):
    return x >= a and x <= b

print(inrange2(3, 2, 4), inrange2(2, 3, 4))

print(9 == 9.0)

print(0.1 + 0.2 + 0.3 == 0)

print(0.1 + 0.2 - 0.3)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

print(l1 + l2, l1, l2)

l3 = l1 + l2
print(l3, l1, l2)

print(l3.append(9))
print(l3)

l3 = l3.append(11)
print(l3)

l3 = l1 + l2
l3 = l3 + [9]
print(l3)

def belongs(v, l):
    for x in l:
        if x == v:
            return True
    return False

print(belongs(8, l3), belongs(12, l3))

def locatepos(v, l):
    pos = 0
    for x in l:
        if x == v:
            return pos
        pos = pos + 1
    return -1

print(locatepos(8, l3), locatepos(12, l3))

def locatepos(v, l):
    pos = 0
    for x in l:
        if x == v:
            return pos
        pos = pos + 1
    return -1

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(locatepos(8, l3), locatepos(12, l3))

print(range(7))

for i in range(7):
    print(i)

l = range(7)
print(type(l))
print(l[2])

l = list(range(7))
print(l)

def locatepos2(v, l):
    for pos in range(len(l)):
        if l[pos] == v:
            return pos
    return -1

print(locatepos2(8, l3), locatepos2(12, l3))

print(list(range(3, 13)))
print(list(range(3, 13, 5)))
print(list(range(3, 13, 3)))
print(list(range(10, 5, -1)))

print(len(l3))
print(list(range(len(l3) - 1, -1, -1)))
print(list(range(len(l3) - 1, -1, -3)))

def factors(n):
    factorlist = []
    for i in range(1, n + 1):
        if n % i == 0:
            factorlist.append(i)
    return factorlist

print(factors(10))

def isprime(n):
    return factors(n) == [1, n]

print(isprime(1), isprime(2), isprime(4))

def primesupto(m):
    primelist = []
    for i in range(1, m + 1):
        if isprime(i):
            primelist.append(i)
    return primelist

print(primesupto(50))
print(primesupto(10000)[-1])

def firstmprimes(m):
    count = 0
    primelist = []
    i = 1
    while count < m:
        if isprime(i):
            primelist.append(i)
            count = count + 1
        i = i + 1
    return primelist

print(firstmprimes(20))
print(len(firstmprimes(20)))

def firstmprimes2(m):
    primelist = []
    i = 1
    while len(primelist) < m:
        if isprime(i):
            primelist.append(i)
        i = i + 1
    return primelist

print(firstmprimes2(15))

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(l), sum(l), max(l), min(l))

def findcommon(l1, l2):
    commonlist = []
    for x in l1:
        for y in l2:
            if x == y:
                commonlist.append(x)
    return commonlist

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print(findcommon(l1, l2))

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 3]
print(findcommon(l1, l2))

for i in range(1000):
    for j in range(1000):
        x = i + j
print("Done")

for i in range(10000):
    for j in range(10000):
        x = i + j
print("Done")

def findcommon(l1, l2):
    commonlist = []
    for x in l1:
        for y in l2:
            if x == y:
                commonlist.append(x)
    return commonlist

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print(findcommon(l1, l2))

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 3]
print(findcommon(l1, l2))

l1 = [1, 2, 3, 4, 3]
l2 = [3, 4, 5, 3]

print(findcommon(l1, l2))

for i in range(1000):
    for j in range(1000):
        x = i + j
print("Done")

for i in range(10000):
    for j in range(10000):
        x = i + j
print("Done")

def duplicates(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                return True
    return False

print(duplicates([1, 2, 3]))
print(duplicates([1, 2, 1]))

def duplicatelist(l):
    dlist = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                dlist.append(l[i])
    return dlist

print(duplicatelist([1, 2, 1]))
print(duplicatelist([1, 2, 1, 3, 1]))

print(1 in [1, 2, 3, 4])

def listcommon2(l1, l2):
    for x in l1:
        if x in l2:
            return True
    return False

def sgn1(v):
    if v > 0:
        return 1
    else:
        if v < 0:
            return -1
        else:
            return 0

def sgn2(v):
    if v >= 0:
        if v > 0:
            return 1
        else:
            return 0
    else:
        return -1

def sgn(v):
    if v > 0:
        return 1
    elif v == 0:
        return 0
    elif v < 0:
        return -1

l = list(range(100))

marks = {'Physics': 75, 'Maths': 88}

for k in marks.keys():
    print(k, marks[k])

for k in marks:
    print(k)

for v in marks.values():
    print(v)

sorted([3, 1, 8, 2, 9])

l = [3, 1, 8, 2, 9]
sorted(l)

l
# sorted(["A",2])
sorted(["B", "A"])
sorted(["1", "2", "3", "10"])

for k in sorted(marks.keys()):
    print(k, marks[k])

for k in sorted(marks):
    print(k, marks[k])

runlist = [("A", 10), ("C", 20), ("A", 44), ("B", 33), ("B", 77)]

totalruns = {}
for p in runlist:
    name = p[0]
    runs = p[1]
    if name in totalruns:
        totalruns[name] = totalruns[name] + runs
    else:
        totalruns[name] = runs

totalrunlist = {}
for p in runlist:
    name = p[0]
    runs = p[1]
    if name in totalrunlist:
        totalrunlist[name] = totalrunlist[name] + [runs]
    else:
        totalrunlist[name] = [runs]

x = input()
print(x, type(x))
print(list(range(10)), range(10))
print(x)
print(str(7888))

# int("abcd")
# int("abcd", 16)

# 13 + 12*16 + 11*16*16 + 10*16*16*16

# list(7)
# list((7,8))

x = input("Please type a number: ")
x = float(x)
print(x)

for k in marks.keys():
    print(k, marks[k])

for k in marks.keys():
    print(k, marks[k], sep=":")

for k in marks.keys():
    print(k, marks[k], sep=":", end="")
    print()

for k in marks.keys():
    print(k, marks[k], sep=":", end=",")

for k in marks.keys():
    print("Name:", k, ", Marks:", marks[k])

count = 0
marksdict = {}
namelist = []
(count, marksdict, namelist) = (0, {}, [])


def myswap(x, y):
    (y, x) = (x, y)


m = 5
n = 10
myswap(m, n)
print(m, n)


def swap(x, y):
    return (y, x)


(m, n) = swap(m, n)
print(m, n)
(m, n) = 5, 10
(m, n) = n, m
print(m, n)

runlist = [("A", 10), ("C", 20), ("A", 44), ("B", 33), ("B", 77)]

totalrunlist = {}
for (name, runs) in runlist:
    if name in totalrunlist:
        totalrunlist[name] = totalrunlist[name] + [runs]
    else:
        totalrunlist[name] = [runs]

y = 17
x = y
x = 15
print(y)

l1 = [1, 2, 3]
l2 = l1[:]
l2[0] = 4
print(l1, l2)

marks
newmarks = marks.copy()
newmarks['Maths'] = 100
print(marks, newmarks)

p1 = (5, 2, 3)
p2 = p1
p1, p2
# p2[1] = 7  # This line was commented out as tuples are immutable and cannot be modified in-place
p2 = (7, 9, 4)
print(p1, p2)

l3 = l1[:]
l1, l3

l3[0] = 17
l1, l3

zeros = [0, 0, 0]
zeromat = [zeros, zeros, zeros]
zeros, zeromat

zeromat[1][1] = 1
zeros, zeromat

zeros = [0, 0, 0]
zeromat2 = [zeros[:], zeros[:], zeros[:]]
zeros, zeromat2

zeromat2[1][1] = 1
zeros, zeromat2

def mycopy(m, n):
    m = n
    a = 5
    b = 7
    mycopy(a, b)
    a, b


l1 = [1, 2]
l2 = [3, 4]
# mycopy(11,l2)  # This line was commented out as the function definition is incomplete
l1, l2


def mycopylist(m, n):
    print(type(m))
    m[0] = n[-1]
    l1 = [1, 2]
    l2 = [3, 4]
    # mycopylist(l1,l2)  # This line was commented out as the function definition is incomplete


l1, l2


def myappend(l, v):
    l.append(v)
    myappend(l2, 5)
    l2


def myappend2(l, v):
    l = l + [v]
    myappend2(l2, 6)
    l2


import time

start = time.perf_counter()
l = []
for i in range(10000000):
    l.append(i)
elapsed = time.perf_counter() - start
print(elapsed)

start = time.perf_counter()
l = []
for i in range(20000000):
    l.append(i)
elapsed = time.perf_counter() - start
print(elapsed)

start = time.perf_counter()
l = []
for i in range(100000):
    l.insert(0, i)
elapsed = time.perf_counter() - start
print(elapsed)

start = time.perf_counter()
l = []
for i in range(200000):
    l.insert(0, i)
elapsed = time.perf_counter() - start
print(elapsed)

start = time.perf_counter()
l = []
for i in range(300000):
    l.insert(0, i)
elapsed = time.perf_counter() - start
print(elapsed)

start = time.perf_counter()
d = {}
for i in range(10000000, 0, -1):
    d[i] = i
elapsed = time.perf_counter() - start
print(elapsed)

start = time.perf_counter()
d = {}
for i in range(20000000, 0, -1):
    d[i] = i
elapsed = time.perf_counter() - start
print(elapsed)

class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x +
        self.y*self.y)
    
        return(d)

p = Point(3,4)
q = Point(7,10)

p.odistance(), q.odistance()

p.translate(3,4)
p.odistance()

print(p)
#print(p+q)
#p < q

import math
class Point:
    def __init__(self,a,b):
        self.r = math.sqrt(a*a + b*b)
        if a == 0:
            if b >= 0:
                self.theta = math.pi/2
            else:
                self.theta = 3*math.pi/2
        else:
            self.theta = math.atan(b/a)
            
    def translate(self,deltax,deltay):
        x = self.r*math.cos(self.theta)
        y = self.r*math.sin(self.theta)
        x += deltax
        y += deltay
        self.r = math.sqrt(x*x + y*y)
        if x == 0:
            if y >= 0:
                self.theta = math.pi/2
            else:
                self.theta = 3*math.pi/2
        else:
            self.theta = math.atan(y/x)
        
    def odistance(self):
        return(self.r)

p = Point(3,4)
q = Point(7,10)

p.odistance(), q.odistance()

p.translate(3,4)
p.odistance()

print(p)
#print(p+q)
#p < q

class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x +
        self.y*self.y)
        return(d)
    
    def __str__(self):
        return('('+str(self.x)+','
        +str(self.y)+')')
    
    def __add__(self,p):
        return(Point(self.x + p.x,
        self.y + p.y))

p = Point(3,4)
q = Point(7,10)

p.odistance(), q.odistance()

p.translate(3,4)
p.odistance()

print(p)
str(p)
print(p+q)
print(p,q)

#p < q


class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x +
        self.y*self.y)
        return(d)
    
    def __str__(self):
        return('('+str(self.x)+','
        +str(self.y)+')')
    
    def __add__(self,p):
        return(Point(self.x + p.x,self.y + p.y))
    
    def __lt__(self,p):
        return(self.x < p.x and self.y < p.y)


p = Point(3,4)
q = Point(7,10)
p < q, q < p

Point.translate(p,9,10)
print(p)

l = [1,2,3]
list.append(l,4)
l
p.x, p.y

class Experiment:
    def __init__(self,a):
        x = a
    def __str__(self):
        return(str(x))
        z = Experiment(5)
        str(z)

class Experiment2:
    def __init__(self,a):
        self.x = a
    def __str__(self):
        return(str(self.x))
        y = Experiment2(7)
        str(y)

class Experiment3:
    def __init__(self,a):
        self.x = a
    def __str__(this):
        return(str(this.x))
    
x = Experiment3(17)
print(x)

class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x +
        self.y*self.y)
    
        return(d)

p = Point(3,4)
q = Point(7,10)

p.odistance(), q.odistance()

p.translate(3,4)
p.odistance()

print(p)
#print(p+q)
#p < q

import math
class Point:
    def __init__(self,a,b):
        self.r = math.sqrt(a*a + b*b)
        if a == 0:
            if b >= 0:
                self.theta = math.pi/2
            else:
                self.theta = 3*math.pi/2
        else:
            self.theta = math.atan(b/a)
            
    def translate(self,deltax,deltay):
        x = self.r*math.cos(self.theta)
        y = self.r*math.sin(self.theta)
        x += deltax
        y += deltay
        self.r = math.sqrt(x*x + y*y)
        if x == 0:
            if y >= 0:
                self.theta = math.pi/2
            else:
                self.theta = 3*math.pi/2
        else:
            self.theta = math.atan(y/x)
        
    def odistance(self):
        return(self.r)

p = Point(3,4)
q = Point(7,10)

p.odistance(), q.odistance()

p.translate(3,4)
p.odistance()

print(p)
#print(p+q)
#p < q

class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x +
        self.y*self.y)
        return(d)
    
    def __str__(self):
        return('('+str(self.x)+','
        +str(self.y)+')')
    
    def __add__(self,p):
        return(Point(self.x + p.x,
        self.y + p.y))

p = Point(3,4)
q = Point(7,10)

p.odistance(), q.odistance()

p.translate(3,4)
p.odistance()

print(p)
str(p)
print(p+q)
print(p,q)

#p < q


class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x +
        self.y*self.y)
        return(d)
    
    def __str__(self):
        return('('+str(self.x)+','
        +str(self.y)+')')
    
    def __add__(self,p):
        return(Point(self.x + p.x,self.y + p.y))
    
    def __lt__(self,p):
        return(self.x < p.x and self.y < p.y)


p = Point(3,4)
q = Point(7,10)
p < q, q < p

Point.translate(p,9,10)
print(p)

l = [1,2,3]
list.append(l,4)
l
p.x, p.y

class Experiment:
    def __init__(self,a):
        x = a
    def __str__(self):
        return(str(x))
        z = Experiment(5)
        str(z)

class Experiment2:
    def __init__(self,a):
        self.x = a
    def __str__(self):
        return(str(self.x))
        y = Experiment2(7)
        str(y)

class Experiment3:
    def __init__(self,a):
        self.x = a
    def __str__(this):
        return(str(this.x))
    
x = Experiment3(17)
print(x)

class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None
        return

    def isempty(self):
        if self.value == None:
            return True
        else:
            return False

    def append(self, v):
        if self.isempty():
            self.value = v
        elif self.next == None:
            self.next = Node(v)
        else:
            self.next.append(v)
        return

    def appendi(self, v):
        if self.isempty():
            self.value = v
            return
        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = Node(v)
        return

    def insert(self, v):
        if self.isempty():
            self.value = v
            return
        newnode = Node(v)
        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)
        return

    def delete(self, v):
        if self.isempty():
            return
        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
            if self.next.value == None:
                self.next = None
            return

    def __str__(self):
        selflist = []
        if self.isempty():
            return str(selflist)
        temp = self
        selflist.append(temp.value)
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)
        return str(selflist)

l = Node()
l.append(5)
print(l)

l.appendi(7)
print(l)

l.append(9)
print(l)

class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None
        return

    def isempty(self):
        if self.value == None:
            return True
        else:
            return False

    def append(self, v):  # append, recursive
        if self.isempty():
            self.value = v
        elif self.next == None:
            self.next = Node(v)
        else:
            self.next.append(v)
        return

    def appendi(self, v):  # append, iterative
        if self.isempty():
            self.value = v
            return
        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = Node(v)
        return

    def insert(self, v):
        if self.isempty():
            self.value = v
            return
        newnode = Node(v)
        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)
        return

    def delete(self, v):  # delete, recursive
        if self.isempty():
            return
        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
            if self.next.value == None:
                self.next = None
            return

    def _tolist(self):
        # Recursively construct a Python list from linked list
        if self.isempty():
            return []
        elif self.next == None:
            return [self.value]
        else:
            return [self.value] + self.next._tolist()

    def __str__(self):
        # Convert Python list representation of linked list to string
        return str(self._tolist())


l = Node()
l.append(5)
print(l)

l.appendi(7)
print(l)

l.delete(7)
print(l)

import time

for i in range(1, 5):
    l1 = Node()
    start = time.perf_counter()
    for j in range(i * 100000):
        l1.insert(j)
    elapsed = time.perf_counter() - start
    print(i * 100000, elapsed)

for i in range(1, 5):
    l2 = []
    start = time.perf_counter()
    for j in range(i * 50000):
        l2.insert(0, j)
    elapsed = time.perf_counter() - start
    print(i * 50000, elapsed)


import time
import sys
sys.setrecursionlimit(2**30-1)
import time


def naivesearch(v,l):
    for x in l:
        if v == x:
            return(True)
    return(False)

def binarysearch(v,l):
    if l == []:
        return(False)
    
    m = len(l)//2
    
    if v == l[m]:
        return(True)
    
    if v < l[m]:
        return(binarysearch(v,l[:m]))
    
    else:
        return(binarysearch(v,l[m+1:]))
    
l = list(range(0,51,2))

for i in range(51):
    print((i,naivesearch(i,l)),end=",")
    print()
for i in range(51):
    print((i,binarysearch(i,l)),end=",")
    print()

l = list(range(0,200000,2))
starttime = time.perf_counter()

for i in range(3001,23000,2):
    v = naivesearch(i,l)
elapsed = time.perf_counter() - starttime
print()
print("Naive search", elapsed)
    
starttime = time.perf_counter()
for i in range(3001,23000,2):
    v = binarysearch(i,l)
elapsed = time.perf_counter() - starttime
print()
print("Binary search", elapsed)


def SelectionSort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        mpos = i

        for j in range(i+1,n):
            if L[j] < L[mpos]:
                mpos = j

        (L[i],L[mpos]) = (L[mpos],L[i])

    return(L)


import random
random.seed(2023)
inputlists = {}
inputlists["random"] = [random.randrange(100000) for i in range(5000)]
inputlists["ascending"] = [i for i in range(5000)]
inputlists["descending"] = [i for i in range (4999,-1,-1)]

for k in inputlists.keys():
    tmplist = inputlists[k][:]
    starttime = time.perf_counter()
    SelectionSort(tmplist)
    elapsed = time.perf_counter() - starttime
    print(k,elapsed)


def Insert(L,v):
    n = len(L)
    if n == 0:
        return([v])
    if v >= L[-1]:
        return(L+[v])
    else:
        return(Insert(L[:-1],v)+L[-1:])

def ISort(L):
    n = len(L)
    if n < 1:
        return(L)
    L = Insert(ISort(L[:-1]),L[-1])
    return(L)

import sys
sys.setrecursionlimit(2**30-1)

import random
random.seed(2023)
inputlists = {}
inputlists["random"] = [random.randrange(100000) for i in range(5000)]
inputlists["ascending"] = [i for i in range(5000)]
inputlists["descending"] = [i for i in range (4999,-1,-1)]
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    starttime = time.perf_counter()
    ISort(tmplist)
    elapsed = time.perf_counter() - starttime
    print(k,elapsed)

def merge(A,B):
    (m,n) = (len(A),len(B))
    (C,i,j,k) = ([],0,0,0)
    while k < m+n:
        if i == m:
            C.extend(B[j:])
            k = k + (n-j)
        elif j == n:
            C.extend(A[i:])
            k = k + (n-i)
        elif A[i] < B[j]:
            C.append(A[i])
            (i,k) = (i+1,k+1)
        else:
            C.append(B[j])
            (j,k) = (j+1,k+1)
    return(C)

def mergesort(A):
    n = len(A)
    if n <= 1:
        return(A)
    
    L = mergesort(A[:n//2])
    R = mergesort(A[n//2:])
    
    B = merge(L,R)
    
    return(B)

mergesort([i for i in range(0,1000,2)]+[j for j in range (1,1000,2)])

import random
random.seed(2023)
inputlists = {}
inputlists["random"] = [random.randrange(100000000) for i in range(1000000)]
inputlists["ascending"] = [i for i in range(1000000)]
inputlists["descending"] = [i for i in range (999999,-1,-1)]
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    starttime = time.perf_counter()
    mergesort(tmplist)
    elapsed = time.perf_counter() - starttime
    print(k,elapsed)
    
def binarysearchiterative(v,L):
    if len(L) == 0:
        return(True)
    left = 0
    right = len(L)
    while (right - left > 0):
        mid = (left + right) // 2
        if v == L[mid]:
            return(True)
        if v < L[mid]:
            right = mid
        else:
            left = mid + 1
    return(False)

evenlist = [n for n in range(50) if n%2 == 0]
print(evenlist)
for i in range(0,60,3):
    print(i,binarysearchiterative(i,evenlist))
    
l = list(range(0,200000,2))
starttime = time.perf_counter()
for i in range(3001,23000,2):
    v = binarysearchiterative(i,l)
elapsed = time.perf_counter() - starttime
print()
print("Binary search", elapsed)

import sys
sys.setrecursionlimit(2**30-1)
import time

def quicksort(L,l,r): # Sort L[l:r]
    if (r - l <= 1):
        return
    
    (pivot,lower,upper) = (L[l],l+1,l+1)
    for i in range(l+1,r):
        if L[i] > pivot: # Extend upper segment
            upper = upper+1
        else: # Exchange L[i] with start of upper segment
            (L[i], L[lower]) = (L[lower], L[i])
            # Shift both segments
            (lower,upper) = (lower+1,upper+1)
    # Move pivot between lower and upper
    (L[l],L[lower-1]) = (L[lower-1],L[l])
    lower = lower-1
    # Recursive calls
    quicksort(L,l,lower)
    quicksort(L,lower+1,upper)
    return

qlist = [1,3,5,0,2,4,17,2,-5,6,4,3]
quicksort(qlist,4,8)
print(qlist)

import random
random.seed(2023)
inputlists = {}
inputlists["random"] = [random.randrange(100000000) for i in range(1000000)]
inputlists["ascending"] = [i for i in range(15000)]
inputlists["descending"] = [i for i in range (14999,-1,-1)]
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    starttime = time.perf_counter()
    quicksort(tmplist,0,len(tmplist))
    elapsed = time.perf_counter() - starttime
    print(k,elapsed)

def quicksortrand(L,l,r): # Sort L[l:r]
    if (r - l <= 1):
        return(L)
    
    # Choose a random postion between l and r-l as pivot, swap with L[l]
    randpivot = random.randrange(r-l)
    (L[l],L[l+randpivot]) = (L[l+randpivot],L[l])

    # Rest is same as before
    (pivot,lower,upper) = (L[l],l+1,l+1)
    for i in range(l+1,r):
        if L[i] > pivot: # Extend upper segment
            upper = upper+1
        else: # Exchange L[i] with start of upper segment
            (L[i], L[lower]) = (L[lower], L[i])
            # Shift both segments
            (lower,upper) = (lower+1,upper+1)
    # Move pivot between lower and upper
    (L[l],L[lower-1]) = (L[lower-1],L[l])
    lower = lower-1
    # Recursive calls
    quicksortrand(L,l,lower)
    quicksortrand(L,lower+1,upper)
    return(L)

random.seed(2023)
inputlists = {}
inputlists["random"] = [random.randrange(100000000) for i in range(1000000)]
inputlists["ascending"] = [i for i in range(15000)]
inputlists["descending"] = [i for i in range (14999,-1,-1)]
inputlists["ascendingbig"] = [i for i in range(1000000)]
inputlists["descendingbig"] = [i for i in range (999999,-1,-1)]

for k in inputlists.keys():
    tmplist = inputlists[k][:]
    starttime = time.perf_counter()
    quicksortrand(tmplist,0,len(tmplist))
    elapsed = time.perf_counter() - starttime
    print(k,elapsed)

print("Select operation.")
print("1.Number system converter")
print("2.Python Numeric data type converter")
print("3.Multiply")
print("4.Divide")

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
                        print("ASCII value: ", ord(value))
                
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

                
                else:
                    print("Invalid Input")

#block3

        elif choice == '3':
            print("Select the Data type to convert")
            print("1.String")
            print("2.List")
            print("3.Tuple")
            print("4.Set")
                  
            while True:
                ch3 = input("Enter choice(1/2/3/4): ")

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

                
                else:
                    print("Invalid Input")

#block
        if choice == '4':
            
            import matplotlib.pyplot as plt

            x = list(input("Enter X co-ordinates seperated with comma : "))
            y = list(input("Enter Y co-ordinates seperated with comma : "))

            plt.plot(x, y, color = 'c', marker = 'h')

            plt.xlabel('x - axis')
            plt.ylabel('y - axis')
             
            plt.title('Required Graph')
             
            plt.show()























            


































            


