# def print2(str1):
#     print2(str1)
#     # print("This is "+ str1)
#
#
# print2("Harry")


# Iterative function
def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac
number = int(input("Enter a No : "))
print("Factorial : ",factorial(number))


# Reccurrence Function


def fact(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)
print("Factorial : ",fact(number))