print("Armstrong Number")
num = int(input("Enter Any 3 Digit Number : "))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum += digit**3
    temp//=10

if num==sum:
    print(num,"is a Armstrong Number")
else:
    print(num,"is not a Armstrong Number")