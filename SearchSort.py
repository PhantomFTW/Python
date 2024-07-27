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
