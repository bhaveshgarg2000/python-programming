def JTOI():
    file = open("D:\SEM-4\PYTHON\LABS\python.txt","r")
    data = file.read()
    for letter in data:
        if letter == 'J':
            print("I",end="")
        else:
            print(letter,end="")

    file.close()

JTOI()