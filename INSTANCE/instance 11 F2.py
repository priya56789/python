
# Q1. Create a class Student that:
# Keeps track of the total number of students created.
# Determines whether a student passed or failed based on a shared passing mark.
# Provides a method to curve marks by increasing everyone’s marks by a percentage.
# Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
# Demonstrate:
# Creating multiple students.
# Applying a grading curve.
# Displaying updated results with letter grades.



class student:
    total_students=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>0:
            return "pass"
        else:
            return "Fail"
    @classmethod
    def curve_marks(cls,students,percentage):
        student.marks+=students.marks*percentage/100
    @staticmethod
    def grade_category(marks):
        if marks>90:
            return "A Grade"
        elif marks>80:
            return "B Grade"
        else:
            return "C Grade"
s1=student("Priyanka",40)
print(s1.grade_category(112))
print(s1.grade_category(82))
