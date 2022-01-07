print("Area of Triangle")
a = int(input("Enter the side a : "))
b = int(input("Enter the side b : "))
c = int(input("Enter the side c : "))
# Semi Perimeter
s = (a+b+c)/2
# Area of Triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle : ',area)