# Q7. Create a class Employee with:
# instance attributes: name, base_salary
# class variable: bonus_rate = 0.1
# instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# class method: update_bonus(cls, new_rate) → updates bonus for all employees
# static method: is_valid_salary(sal) → checks if salary > 0
# Create two employees, show final salaries, update bonus rate, and show again.



class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        final_salary=self.base_salary+(self.base_salary*self.bonus_rate)
        print(final_salary)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        if sal>0:
            return True
        else:
            return False
employee1=Employee("Eswar",1000)
employee2=Employee("Priyanka",2000)
print(employee1.final_salary())
print(employee2.final_salary())
Employee.update_bonus(0.5)
employee1.update_bonus(1.5)
employee2.update_bonus(2.5)
print(Employee.bonus_rate)
print(employee1.bonus_rate)
print(employee2.bonus_rate)
print(employee1.is_valid_salary(20000))
print(employee2.is_valid_salary(30000))
