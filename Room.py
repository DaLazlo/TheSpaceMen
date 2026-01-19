from enum import Enum

from Weapons import *
from SpaceMan import *

class RoomType(Enum):
    HALLWAY = "HallWay"
    ENGINEROOM = "EngineRoom"
    BRIDGE = "Bridge"
    MESSHALL = "MessHall"
    MEDBAY = "MedBay"

class Room():
    def __init__(self, roomtype):
        inventory = []
        match roomtype:
            case RoomType.HALLWAY:
                self.type = RoomType.HALLWAY
                self.inventory = []
                self.spacemen = []
                self.aliens = []
                self.destinations = [ RoomType.BRIDGE, RoomType.ENGINEROOM, RoomType.MEDBAY, RoomType.MESSHALL, ]
            case RoomType.ENGINEROOM:
                self.type = RoomType.ENGINEROOM
                self.inventory = [ WeaponType.EXTINGUISHER, ]
                self.spacemen = [ Crew.ENGINEER, ]
                self.aliens = []
                self.destinations = [ RoomType.HALLWAY ]
            case RoomType.BRIDGE:
                self.type = RoomType.BRIDGE
                self.inventory = [ WeaponType.PISTOL ]
                self.spacemen = [ Crew.CAPTAIN ]
                self.aliens = []
                self.destinations = [ RoomType.HALLWAY ]
            case RoomType.MESSHALL:
                self.type = RoomType.MESSHALL
                self.inventory = [ WeaponType.CLEAVER ]
                self.spacemen = [ Crew.COOK ]
                self.aliens = []
                self.destinations = [ RoomType.MESSHALL ]
            case RoomType.MEDBAY:
                self.type = RoomType.MEDBAY
                self.inventory = [ WeaponType.SYRINGE ]
                self.spacemen = [ Crew.MEDIC ]
                self.aliens = []
                self.destinations = [ RoomType.HALLWAY ]

    def take_turn(self):
        # act, spacemen only
        for spaceman in self.spacemen:
            spaceman.act(self)

        # attack, spacemen first
        for spaceman in self.spacemen:
            spaceman.attack()
        for alien in self.aliens:
            alien.attack()
        
        # move, only if no enemies present
        if len(self.aliens) == 0:
            for spaceman in self.spacemen:
                spaceman.move()
        elif len(self.spacemen) == 0:
            for aleint in self.aliens:
                alien.move()
        
        # grow, aliens only
        for alien in self.aliens:
            alien.grow(self)

    def addInventory(self, weapon: Weapon):
        self.inventory.append(weapon)

    def removeInventory(self, weapon: Weapon):
        self.inventory.remove(weapon)
