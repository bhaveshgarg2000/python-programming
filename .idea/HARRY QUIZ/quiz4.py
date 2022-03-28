a = int(input("Enter the number of rows you want in the star pattern : "))
b = bool(int(input("Enter 1 if you want straight star pattern \n"
                   "Enter 0 if you want inverted star pattern \n")))
if b == True :
    for i in range(a) :
        print((i+1)*"*")
elif b == False :
    while a != 0 :
        print(a*"*")
        a = a-1