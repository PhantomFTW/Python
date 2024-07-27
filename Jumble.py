def jumble(a):
    str = ''

    for i in range(len(a)):
        if a[i].islower():
            str = str + a[i].upper()
        elif a[i].isupper():
            str = str + a[i].lower()
        elif a[i].isdigit():
            str = str + '*'
        else:
            str = str + '@'

    return str

a = input("Enter a string: ")
print("Your jumbled string is: ", jumble(a))
