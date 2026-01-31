from enum import Enum


from Weapons import *
from Effect import *
from Room import Room
from Alien import Alien

from random import randint, choice

class Crew(Enum):
    CAPTAIN = "Captain Zog"
    ENGINEER = "Engineer Dro"
    MEDIC = "Medic Lep"
    COOK = "Cook Bel"

class SpaceMan():
    punchEffect = None

    def __init__(self, crewmember):
        self.health = 10
        self.weapon = None
        match (crewmember):
            case Crew.CAPTAIN:
                self.name = "Captain Zog"
            case Crew.ENGINEER:
                self.name = "Engineer Dro"
            case Crew.MEDIC:
                self.name = "Medic Lep"
            case Crew.COOK:
                self.name = "Cook Bel"

    def takeDamage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage")
    
    def attack(self, target: Alien, room: Room):
        if self.weapon != None:
            if self.weapon.effect == None:
                self.weapon.effect = getRandomEffect()
                print(f"{self.weapon.name} is discovered to have {self.weapon.effect.value} effect")
            print(f"{self.name} attacks {target.name} with {self.weapon.name} (effect: {self.weapon.effect.value})")
            target.applyEffect(self.weapon.effect, room)
        else:
            if SpaceMan.punchEffect == None:
                SpaceMan.punchEffect == getRandomEffect()
            elif not SpaceMan.punchEffect in BadEffects:
                target.applyEffect(SpaceMan.punchEffect)
    
    def act(self, room: Room):
        # pick up a (good) weapon if I don't have one
        if self.weapon == None:
            for weapon in room.inventory:
                if not weapon.effect in BadEffects:
                    self.weapon = weapon
                    room.removeInventory(weapon)
                    print(f"{self.name} picks up {self.weapon.name}")
                    return
        # drop ineffective weapon
        elif self.weapon.effect in BadEffects:
            print(f"{self.name} drops {self.weapon.name} since it is useless")
            room.addInventory(self.weapon)
            self.weapon = None
            return
                
    def move(self, room: Room):
        destination = choice(room.destinations)
        print(f"{self.name} moves from {room.name} to {destination.name}")
        destination.spacemen.append(self)
        room.spacemen.remove(self)
        
