# Create two classes Father and Mother, both defining a method skills(). Create
# class Child(Father, Mother) and check which skills() runs using MRO.




class Father:
    def skills(self):
        print("going to ofc")
        super().skills()
class Mother:
    def skills(self):
        print("Cooking")
class child(Father,Mother):
    def skills(self):
        super().skills()
        print("Studying")
obj=child()
obj.skills()

