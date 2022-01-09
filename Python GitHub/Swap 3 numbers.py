print("SWAP 3 NUMBERS")
a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))
c = int(input("Enter value of c :"))
# Two numbers swap
# a , b = b,a
# print(a,b)

# 3 NO SWAPPING

temp = a
a = b
b = c
c = temp

print("The VALUE OF A after SWAPPING is : {}".format(a))
print("The VALUE OF B after SWAPPING is : {}".format(b))
print("The VALUE OF C after SWAPPING is : {}".format(c))
# print(a,b,c)