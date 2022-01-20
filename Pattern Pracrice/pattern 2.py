n = int(input("Enter the no of Row you want : "))
for i in range(n):
    for j in range(i,-1,-1):
        print(j+1,end = " ")
    print()