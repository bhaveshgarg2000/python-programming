z =['Python', 'C#', 'JavaScript']
print(len(z))
print(z[0])
z[0] = "C++"
print(z[0])

print("\n")
for x in z:
    print(x)


z.append("HTML")
print(z)


z.pop(1)
print(z)



z.remove("HTML")

# print(a)

# a.reverse()
# a.sort()
# print(a)
b = z.copy()
print("\nB")
print(b)

print("\nA")
print(z)


a = 2
n =8.3
print(a+n)