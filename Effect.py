from enum import Enum
from random import randint


class EffectType(Enum):
    DAMAGE1 = "Cause 1 Damage"
    DAMAGE2 = "Cause 2 Damage"


class Effect():
    def __init__(self):
        pass

    def attack(self, target):
        match (randint(0,1)):
            case 0:
                self = Damage_One(target)
            case 1:
                self = Damage_Two(target)

class Damage_One(Effect):
    def __init__(self, target):
        self.attack(target)
    
    def attack(self, target):
        # do an attack one to target
        pass

class Damage_Two(Effect):
    def __init__(self, target):
        self.attack(target)
    
    def attack(self, target):
        # do an attack two to target
        pass


