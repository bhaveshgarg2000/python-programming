list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# list[4] = "Time"
list[1:] = ["blackcurrant", "watermelon"]
# print(list)
# print(list[1])
# print(list[2])


list.insert(0,"COLA")
list.append("COCA")
# print(list)


A = ["Deven","Swastik","Kunal"]
B = ["Bhavesh"]
C = ["Bhavuk","Kunal"]
A.extend(B)
A.extend(C)
# print(A)



A.remove("Deven")
print(A)
# Pop element by index location
A.pop(1)
print(A)
A.pop()
print(A)
# Remove first element

del A[0]
print(A)
DD = ["Banana","Mango","Grapes"]
# del DD
DD.clear()
print(DD)