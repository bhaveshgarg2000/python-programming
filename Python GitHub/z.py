# for number in range(1,5):
#     print ("The current number is ",number)
# print("---------------------------")
# for number in range(1,7,2):
#     print ("The current number is ",number)
# print("---------------------------")
# for number in range(5,0,-1):
#     print ("The current number is ",number)

# for passenger in "A","A", "FC", "C", "FA", "SP", "A", "A":
#     if(passenger=="FC" or passenger=="FA"):
#         print("No check required")
#         continue
#     if(passenger=="SP"):
#         print("Declare emergency in the airport")
#         break
#     if(passenger=="A" or passenger=="C"):
#         print("Proceed with normal security check")
#     print("Check the person")
#     print("Check for cabin baggage")
#
# num1=100
# num2=200
# num3=6
# if(5>=num3):
#     if(num1>100 or num2>150):
#         print("1")
# elif(num1>=100 and num2>150):
#     print("2")
# else:
#     print("3")

#
# num1 = 10
# num2 = 2
# if((num1/num2==5) and (num1+num2)>5):
#     print("1")
# elif((num1-num2)<=1 or (num1%num2)==0):
#     print("2")
# else:
#     print("3")

# a = -10
# b = -200
# c = 2000
# d = 4000
# if( a*b >=d):
#     if(d>c):
#         if(d%c!=0):
#             print(11)
#         else:
#             print(22)
# else:
#     if(b/a >0):
#         if(a<b or d%c!=0):
#             print(33)
#         else:
#             print(44)

# for number in 10,15:
#     for counter in range(1,3):
#         print(number*counter, end=" ")

# number=28
# for num in range(25,30):
#     if(number>num):
#         print(num)
#     else:
#         print(num)
#         break

# for num in 23, 45, 50, 65, 76, 90:
#     if(num%5!=0):
#         continue
#     if(num%10==0):
#         print(num, end=" ")
#         continue
#     if(num%3==0):
#         print(num, end=" ")

#
# observe1="What's happening!!"
# def passport_check(passport_no):
#     observe4="actual copied to formal"
#     observe5="func. execution starts"
#     if(len(passport_no)==8):
#         if(passport_no[0]>="A" and passport_no[0]<="Z"):
#             status="valid"
#         else:
#             status="invalid"
#     else:
#         status= "invalid"
#     observe6="func. execution ends"
#     return status
# observe2="function with formal arg."
# observe3="calling with actual arg."
# passport_status=passport_check("M9993471")
# print("Passport is",passport_status)
# #observe1,2,3,4,5,6 are temporary variables used to explain this concept
#
# def collect_tax(x,y):
#     tax=x+y
#     return tax
#
# a=5000
# b=12000
# result=collect_tax(a,b)
# print(result)
#
#
# result=0
#
# def find_sum(num1,num2):
#     if(num1!=num2):
#         result=num1+num2
#     else:
#         result=2*(num1+num2)

# find_sum(3,4)
# print(result)
# find_sum(5,5)
# print(result)

