# Create class University with a class variable and a class method. Inherit it
# into class College and access the parent’s class variable from the child class.


class University:
    university_name="Andhra university"
    @classmethod
    def change_university(cls,new):
        cls.university_name=new
class College(University):
    def show_university(self):
        return self.university_name
obj=College()
obj.change_university("KL University")
print(obj.show_university())
