class Vehicle:

    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity



    def Sisplay(self):
        print("Vehicle Name : ",self.name)
        print("vehicle Capacity : ",self.capacity)

D1 = Vehicle("TUV 3OO","8")

D1.Sisplay()