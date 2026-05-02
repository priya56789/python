# Q5. Create a class Course that:
# Tracks total courses created.
# Each course has a title, duration, and enrolled_students.
# Provides a method to enroll a new student.
# Allows updating the minimum duration for a valid course across all instances.
# Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# Creating multiple courses.
# Enrolling students.
# Updating minimum duration and checking durations.



class Course:
    total_courses = 0
    minimum_duration = 4

    def __init__(self, title, duration, enrolled_students):
        self.title = title
        self.duration = duration
        self.enrolled_students = enrolled_students

    def enroll(self):
        self.enrolled_students += 1

    @classmethod
    def update_minimum_duration(cls, new_minimum_duration):
        cls.minimum_duration = new_minimum_duration

    @staticmethod
    def is_duration_realistic(duration):
        if duration > 0:
            return True
        else:
            return False


student1 = Course("Python", 4, 2)
student2 = Course("Datascience", 6, 5)
print(student1.title, student1.duration, student1.enrolled_students)
print(student2.title, student2.duration, student2.enrolled_students)
print(student1.enroll())
print(student2.enroll())
Course.update_minimum_duration(8)
print(Course.minimum_duration)
print(Course.is_duration_realistic(8))
print(Course.is_duration_realistic(-2))

