class Employee:
        def __init__(self,name,salary):
            self.emp_name = name
            self.emp_salary = salary

        def displayEmployeeInfo(self):
            print ("Employee name is ",self.emp_name,'and his salary is ',self.emp_salary)

emp1 = Employee('Kousik', 1000)

emp1.displayEmployeeInfo()