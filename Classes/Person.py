class Person:

    def __init__(self,name,age,sex,location,religion,birth_location,father,mother):
        self.name = name
        self.age = age
        self.sex = sex
        self.location = location
        self.religion = religion
        self.birth_location = birth_location
        self.father = father
        self.mother = mother


    def display(self):
        print("Person Details : ")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Sex : ",self.sex)
        print("Location : ",self.location)
        print("Religion : ",self.religion)
        print("Birth Location : ",self.birth_location)
        print("Father : ",self.father)
        print("Mother : ",self.mother)


Details = Person("BHAVESH KRISHAN GARG","21","MALE","NEW DELHI","HINDUSIM","AMBALA","PANKAJ","ANTEEM")


Details.display()