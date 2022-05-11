x = 300

def myfun():
    global x
    x = 200
    print("Inside Function : ",x)

myfun()

print("Outside Function : ",x)