def swap(a,b):
    temp = a
    a = b
    b = temp
    print("Numbers After Swapping : ",(a,b))
num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
print("Numbers Before Swapping ",(num1,num2))
swap(num1,num2)

