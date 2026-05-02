# Q10. Create a class Student with:
# class variable passing_marks = 40
# instance attributes name, marks
# instance method result() → prints pass/fail using class variable
# class method update_passing_marks(cls, new_marks)
# static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# Creates students
# Updates the passing criteria
# Displays grade category and result


class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>0:
            return "pass"
        else:
            return "Fail"
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>90:
            return "A grade"
        elif marks>80:
            return "B grade"
        else:
            return "C grade"
s1=Student("Priyanka",40)
s2=Student("Eswar",55)
Student.update_passing_marks(10)
print(Student.passing_marks)
print(Student.grade_category(40))
