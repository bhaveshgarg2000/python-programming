list1 = [1,"ABC",2,3,5,6,"S0","A",99,7,66,321]
for item in list1:
    if type(item) == int and item > 6:
        print(item)