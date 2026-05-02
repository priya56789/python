# 6. Create a Character class with:
# • private _health
# • methods to damage(points) and heal(points)
# • health cannot drop below 0 or exceed max limit
# • expose only current health through a read-only getter

class Character:
    def __init__(self,health):
        self.__health=health
        self.__max=100
    def damage(self,points):
        self.__health=max(0,self.__health-points)
    def heal(self,points):
        self.__health=min(self.__health,self.__health+points)
    def get_health(self):
        return self.__health
obj=Character(100)
obj.damage(50)
obj.heal(80)
print(obj.get_health())