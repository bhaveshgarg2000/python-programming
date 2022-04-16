class Intro:

    def __init__(self,name,age,contact):
        self.name = name
        self.age = age
        self.contact = contact


    def display(self):
        print("My Name is : ",self.name)
        print("Age : ",self.age)
        print("Contact : ",self.contact)


Name = Intro("BHAVESH KRISHAN GARG","21","+91 8882636499")
# Name.age = "5"
Name.display()



