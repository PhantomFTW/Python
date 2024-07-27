import random

l = []
length = int(input("Enter the length of the list: "))
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

for i in range(length):
    l.append(random.randint(lower, upper))

print("Your final list is: ")
print(l)