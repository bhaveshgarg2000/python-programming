list1 = ["Apple","Banana","Grapes"]
list2 = [1,3,5,7,9]
list3 = ["Apple",1,"Banana",2,"Grapes",3]

print(list1[-1])
print(list2[2])

print(list3[0:3])
print(list3[-3:-1])


# Item exist in List

if "Apple" in list3:
    print("Yes, Apple Found!!")


if "Apple" not in list2:
    print("Apple,Not Found!!")