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
