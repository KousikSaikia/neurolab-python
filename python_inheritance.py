class Person:

    def __init__(self,name):
        self.name = name

    def displayName(self):
        print(self.name, " is a good boy")

    def isEmploeed(self):
        print(self.name, " is not employeed")

class Employee(Person):

    def __init__(self, name,salary,id,designation):
        
        self.salary = salary
        self.id = id
        self.designation = designation

        #Calling constructor of base class
        #Person.__init__(self,name)
        super().__init__(name)

    def isEmplyeed(self):
        print(self.name, " is an employee")

emp1=Person('Hari')
emp1.displayName()
emp1.isEmploeed()

emp=Employee('Kousik',1000,21,'SVP')
emp.displayName()
print(emp.salary)