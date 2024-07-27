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