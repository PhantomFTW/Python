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
