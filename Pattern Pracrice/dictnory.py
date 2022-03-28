dict = {
    "Name":"BHAVESH",
    "BRANCH":"CSE",
    "YEAR":"2020-2024"
}
print(dict)
print(dict.items())
print(dict.values())
print(dict.get("Name"))
# print(dict.clear("Name"))
print(dict.update({"Branch":"CSTI"}))
print(dict)
print(dict.keys())

# if "N" in dict:
#     print("Yes Name Exists in Dictionary")
# else:
#     print("No,Not Exists")


dict["Pacakage"] = "25 L.P.A"
print(dict)
print(dict.pop("Branch"))
print(dict)
dict.popitem()
print(dict)
del dict["Name"]
print(dict)

dict.clear()
print(dict)