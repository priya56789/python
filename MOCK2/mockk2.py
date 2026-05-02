from os import name

'''nums=[5,10,36,2,85,65,45,20,15]
result=list(map(lambda x:((x*x)-x),nums))
print(result)

nums=[5,10,25,90,110,205,310,55,360]
result=list(filter(lambda x:0<=x<=255,nums))
print(result)

from functools import reduce
result1=reduce(lambda x,y:x+y,nums)
print(result1)'''



'''class wifi:
    def __init__ (self,wifi_name,pass_word):
        self.wifi_name=wifi_name
        self.__password=pass_word
class  Building:
    def __init__ (self,rooms:int,floors_int,lift_bool,building_name:str):
        self.rooms=rooms
        self.floors=floors
        self.lift=lift
        self.bulding_name=bulding_name
    def get_password(self):
        if self.wifi_available():
            return self.__password
        else:
            print("wifi not available")
    def set_password(self,new):
        if self.wifi_available():
            self.__password=new
    def __str__(self):
        return self.wifi_name
    def __repr__(self):
        return self.wifi_name'''


'''class Modes:
    def __init__(self,modes):
        self.modes=modes
class Fan(Modes):
    def __init__(self,brand,modes):
        self.brand=brand
        if 3<=modes<=5:
            super().__init__(modes)
        else:
            print("None")
class Ac(Modes):
    def __init__(self,brand,modes):
        self.brand=brand
        if modes==3 or modes==4:
            super().__init__(modes)
        else:
            self.modes=None
    def __str__(self):
        return f"Brand name:{self.modes},No of Modes:{self.brand}"
obj=Fan("fan brand",3)
obj1=Ac( "brand",4)
print(obj.__str__())
print(obj1.__str__())'''

class wifi:
    def __init__(self,wifi_name,password):
        self.wifi_name=wifi_name
        self.__password=password
class Building:
    def __init__(self,rooms:int,floors:int,lift:bool,building_name:str):
        self.rooms=rooms
        self.floors=floors
        self.lift=lift
        self.bulding_name=building_name
class Hostel(wifi,Building):
    def __str__(self):
        return f"rooms:{self.rooms},floors:{self.floors},lift:{self.lift},building_name:{self.building_name}"
    def __repr__(self):
        return self.__str__()

    def __add__(self,other):
        return self.rooms+other.rooms
    def __get_password__(self):

        return self.__get_password__()




