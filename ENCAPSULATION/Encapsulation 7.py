# 7. Create:
# • An Engine class with private state like temperature
# • A Car class that uses an Engine but should:
# o Not allow users to manipulate engine temperature
# o Only expose methods like start_car() or cool_engine()
# Demonstrate why giving direct engine access is dangerous.

class engine:
    def __init__(self,temp):
        self.__temp=30
    def cool(self):
        self.__temp-=10
    def show(self):
        return self.__temp
class Car:
    def __init__(self):
        self.__engine=engine(20)
    def start_car(self):
        print("Car Start")
    def cool_engine(self):
        self.__engine.cool()
        print(self.__engine.show())
c=Car()
c.start_car()
c.cool_engine()
