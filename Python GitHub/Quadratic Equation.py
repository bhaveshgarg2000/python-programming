import cmath

print("Quadrartic Equation problem")

a = int(input("Enter the value of A : "))
b = int(input("ENter the value of B : "))
c = int(input("ENter the value of C : "))
d = ((b**2)-(4*a*c))

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The Solution are {0} and {1}".format(sol1,sol2))