print("😊😊😊😊😊😊😊😊😊😊😊")
print("Prime Number")
a = int(input("Enter Number : "))
flag = False
if a>1:
    for i in range(2,a):
        if(a%i)== 0:
            flag = True
            break
if flag:
    print(a," is not Prime Number.")
else:
    print(a," is a Prime Number")
print("😊😊😊😊😊😊😊😊😊😊😊")