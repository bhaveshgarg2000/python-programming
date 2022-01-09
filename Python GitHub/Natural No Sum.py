print("Natural No Sum")
n = int(input("Enter No of Your Choice : "))
# n = 16
if n<0:
    print("Enter a Positive Number")
else:
    sum = 0
    while(n>0):
        sum = sum + n
        n-=1
print("The Sum is : ",sum)

# Sum of natural numbers up to num

# num = 16
#
# if num < 0:
#     print("Enter a positive number")
# else:
#     sum = 0
#     # use while loop to iterate until zero
#     while(num > 0):
#         sum += num
#         num -= 1
#     print("The sum is", sum)
