print("Fibonacci Series")
n = int(input("Enter the value of 'n': "))
a = 1
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b