fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = [x if x != "banana" else "orange " for x in fruits]
print(new)