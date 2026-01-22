from enum import Enum


from Weapons import *
from Effect import *
from Room import Room
from Alien import Alien

from random import randint

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
    
    def attack(self, target: Alien):
        if self.weapon != None:
            if self.weapon.effect == None:
                self.weapon.effect = getRandomEffect()
            target.applyEffect(self.weapon.effect)
        else:
            if SpaceMan.punchEffect == None:
                SpaceMan.punchEffect == getRandomEffect()
            if not SpaceMan.punchEffect in BadEffects:
                target.applyEffect(SpaceMan.punchEffect)
    
    def act(self, room: Room):
        # drop ineffective weapon
        if self.weapon.effect in BadEffects:
            room.addInventory(self.weapon)
            self.weapon = None
            return
        # pick up a (good) weapon if I don't have one
        if self.weapon == None:
            for weapon in room.inventory:
                if not weapon.effect in BadEffects:
                    self.weapon = weapon
                    room.removeInventory(weapon)
                    return
                
    def move(self, room: Room):
        destination = randint(0, len(room.destinations)-1)
        room.destinations[destination].spacemen.append(self)
        room.spacemen.remove(self)
        
