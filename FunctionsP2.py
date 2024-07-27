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
