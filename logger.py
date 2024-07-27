def log(lt):
    with open("logged data.txt",'a') as f:
        str1 = ""
        for i in lt:
            for j in i:
                str1 += str(j) + "\n"
        f.write(str1)


def show():
    with open("logged data.txt", 'r') as f:
        text = f.read()
    print(text)





