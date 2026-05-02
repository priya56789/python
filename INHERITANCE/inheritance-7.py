# Create class MathOps with a static method add(a, b). Create class
# AdvancedOps(MathOps) and use the static method without overriding it.

class Mathops:
    @staticmethod
    def add(a,b):
        return a+b
class Advancedops(Mathops):
    pass
obj=Advancedops()
print(obj.add(5,3))
