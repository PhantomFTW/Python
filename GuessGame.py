import random

limit = 0
guess = 0

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

sec_num = random.randint(lower, upper)

if sec_num <= 10 and sec_num >=0:
    limit = 3
elif sec_num <= 50 and sec_num >= 0:
    limit = 5
elif sec_num <= 100 and sec_num >= 0:
    limit = 10
else:
    limit = 15

while guess < limit:
    guesss = int(input("Enter your guess: "))
    if guesss != sec_num:
        print("Sorry, you lost, try again.")
        guess += 1
    elif guesss == sec_num:
        print("You won!")

        break