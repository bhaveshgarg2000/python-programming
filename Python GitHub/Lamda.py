# x = lambda a : a+10
# print(x(5))


# a = lambda a,b,c : a+b+c
# print(a(5,6,7))

# x = lambda a, b : a*b
# print(x(5,4))


def func(n):
    return lambda a : a*n

b =  func(5)
print(b(5))