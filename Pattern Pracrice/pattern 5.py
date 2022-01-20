n = int(input("Enter the no of Rows u want : "))
for i in range(n):
    for j in range(i+1):
        print(n-j,end=" ")
    print()