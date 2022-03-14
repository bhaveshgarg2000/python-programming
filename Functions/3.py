def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact =fact*i
    return fact


# result = factorial(n)
N = int(input("Enter the Number : "))
print("The Factorial of Number: %d",(N))


