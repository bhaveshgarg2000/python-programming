print("Welcome")
Name = input("Enter Username : ")
try:
    number = int(Name)
    print(number)
except:
    print("Invalid Username")