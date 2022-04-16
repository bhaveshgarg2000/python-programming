class Laptop:

    def __init__(self,name,processor,ram,hdd,cost,year):
        self.name = name
        self.processor = processor
        self.ram = ram
        self.hdd = hdd
        self.cost = cost
        self.year = year


    def details(self):
        print("Details of Laptops : ")
        print("Name :",self.name)
        print("Processor :",self.processor)
        print("Ram : ",self.ram)
        print("HDD : ",self.hdd)
        print("Cost : ",self.cost)
        print("Year : ",self.year)

laptop1 = Laptop("HP 15 pavillion","INTEL CORE i5","16GB","25GB","85K","2021")

print(laptop1.name)
print(laptop1.year)

laptop1.details()