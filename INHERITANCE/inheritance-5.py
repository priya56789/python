# Create class Employee with an instance method salary(). Create class
# Manager(Employee) that overrides salary() and adds an incentive. Demonstrate
# both outputs.


class Employee:
    def __init__ (self,base_salary):
        self.base_salary= base_salary
    def salary(self):
        return self.base_salary
class Manager(Employee):
    def __init__ (self,base_salary,incentive):
        super().__init__(base_salary)
        self.incentive=incentive
    def salary(self):
        return super().salary()+self.incentive
obj=Manager(20000,6000)
print(obj.salary())
obj=Employee(30000)
print(obj.salary())