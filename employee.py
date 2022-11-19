class Employee:

    count = 0

    def __init__(self,name,age,dept):

        self.name = name
        self.age = age
        self.department = dept
        Employee.count +=1

emp1=Employee('Kousik', 24, 'Electrical')
emp2=Employee('Rcd', 24, 'Electrical')
print(Employee.count)