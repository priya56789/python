# 4.Design an Employee class where:
# • salary is hidden
# • outsiders cannot read salary directly
# • use getter method that logs each access attempt
# • provide a method to update salary but only if the new salary is higher (prevent
# accidental downgrade)


class Employee:
    def __init__ (self,salary):
        self.__salary=salary
    @property
    def get_salary(self):
        return self.__salary
    @get_salary.setter
    def get_salary(self,new):
        if new>self.__salary:
            self.__salary=new
        else:
            print("No Change")
emp=Employee(20000)
print(emp.get_salary())
emp.update_salary(50000)
print(emp.get_salary())