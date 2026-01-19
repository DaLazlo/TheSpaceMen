
from SpaceMan import SpaceMan

from Effect import EffectType
from Room import Room

class Alien():
    def __init__(self, stage):
        match (stage):
            case 0:
                self.health = 2
                self.name = "Egg"
                self.stage = 0
            case 1:
                self.health = 2
                self.name = "Alien"
                self.stage = 1
            case 2:
                self.health = 2
                self.name = "Elder Alien"
                self.stage = 2
    
    def attack(self, target: SpaceMan):
        target.takeDamage(1)
    
    def grow(self, room: Room):
        if self.stage == 0:
            self.stage = 1
            self.name = "Alien"
        elif self.stage == 1:
            self.stage = 2
            self.name = "Elder Alien"
        else:
            room.aliens.append(Alien(0))
            room.aliens.append(Alien(0))
            room.aliens.remove(self)


    def applyEffect(self, effect: EffectType):
        match (effect):
            case EffectType.DAMAGE1:
                self.takeDamage(1)
            case EffectType.DAMAGE2:
                self.takeDamage(2)

    def takeDamage(self, damage):
        self.health -= damage

    def move(self, room: Room):
        destination = randint(0, len(room.destinations)-1)
        room.destinations[destination].aliens.append(self)
        room.aliens.remove(self)
    