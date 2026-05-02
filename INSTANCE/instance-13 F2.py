# Q3. Create an Employee class that:
# Keeps a minimum experience required for promotion (shared across all employees).
# Stores employee name, experience, and department.
# Has a method to check eligibility for promotion.
# Provides a function to update promotion criteria globally.
# Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# Creating employees from different departments.
# Changing promotion criteria.
# Displaying eligibility results and department validation.





class Employee:
    minimum_experience=3
    def  __init__  (self,employee_name,experience,department):
        self. employee_name= employee_name
        self.experience=experience
        self.department=department
    def is_eligible(self):
        if   self.experience >=3:
                    return True
        else:
                    return False
    @classmethod
    def update_promotion_criteria(cls,new_experience):
        cls.minimum_experience=new_experience
        @staticmethod
        def department_is_valid(dept):
            if dept in ("HR","Tech","Admin"):
                return "eligible"
            else:
                return "ineligible"
employee1=Employee("Priyanka","3 years","Engineering")
employee2=Employee("Varalakshmi","5 Years","Software")
Employee.update_promotion_criteria(5)
print(Employee.minimum_experience)