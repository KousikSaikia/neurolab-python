class Person:

    def __init__(self,name):
        self.name = name

    def displayName(self):
        print(self.name)

    def isEmploeed(self):
        print(self.name, " is not employeed")

class Employee(Person):
    def isEmplyeed(self):
        print(self.name, " is an employee")

emp1=Person('Hari')
emp=Employee('Kousik')
emp.displayName()
emp.isEmplyeed()
emp1.displayName()
emp1.isEmploeed()