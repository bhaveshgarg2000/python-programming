print("Factorial of Number")
a = int(input("Enter the No : "))
fact = 1
if a<0:
    print("Soory Factorial does exist for Negative Number")
elif a==0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1,a+1):
        fact = fact*i
    print("The Factorial of ",a , " is ",fact)