n = int(input("Enter the np of rows u want : "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()