# l = 10
# def abc(m):
#     global l
#     l+=5
#     m = 33
#     print(l,m)
#     print("hello",m)
# abc("bhavesh")
# print(l)

x = 89
def harry():
    x = 20
    def rohan():
        # it will check the check outside the harry()
        global x
        x = 90
    print("Before Calling rohan()",x)
    rohan()
    print("After calling rohan()",x)


harry()
print(x)