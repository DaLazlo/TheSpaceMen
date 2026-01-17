
from SpaceMan import SpaceMan

from Effect import *

class Alien():
    def __init__(self):
        self.health = 2
        self.name = "Alien"
    
    def attack(self, target: SpaceMan):
        target.takeDamage(1)
    
    def grow(self):
        pass

    def applyEffect(self, effect: EffectType):
        match (effect):
            case EffectType.DAMAGE1:
                self.takeDamage(1)
            case EffectType.DAMAGE2:
                self.takeDamage(2)

    def takeDamage(self, damage):
        self.health -= damage
    