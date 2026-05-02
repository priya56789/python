# Q8. Create a class Course with:
# class variable total_students
# instance variable student_name
# instance method enroll() → increments total_students
# class method show_total(cls) → prints total students
# static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.




class  Course:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total_students(cls,new):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        if age>=18:
            return True
        else:
            return False
student=Course("Priyanka")
Course.enroll(10)
Course.show_total_students(20)
print(student.student_name)
print(student.enroll())
print(student.is_eligible(12))
