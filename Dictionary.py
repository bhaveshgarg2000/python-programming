d1 = {};
# print(d1)
# print(type(d1))

d2 = {"Harry":"Burger","Chirag":"Samosa","Aman":"Pizza","Shubham":{"B":"Roti","L":"Rice","D":"Maggi"}};
# print(d2["Shubham"])
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
print(d2)
del d2[420]
print(d2)

d3 = d2.copy();
del d3["Harry"]
d2.update({"Leena":"Chowmein"})
# print(d3)
print(d2.items())
