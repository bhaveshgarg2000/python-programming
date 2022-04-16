

class Employee:

    def __init__(self,first,last,email,contact):
        self.first = first
        self.last = last
        self.email = email
        self.contact = contact

    def full_name(self):
        print('{} {}'.format(emp_1.first,emp_1.last))



emp_1 = Employee("BHAVESH","GARG","BHAVESHGARG2005@GMAIL.COM","8882636499")
emp_2 = Employee("BHAVESH","GARG","BHAVESHGARG2005@GMAIL.COM","8882636499")

emp_2.full_name()