def hcf(x, y):
    if y == 0:
        return x
    return hcf(y, x%y)

x = 250
y = 475

print("HCF of", x, "and", y, "is:", hcf(x,y))