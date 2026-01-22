from enum import Enum


class RoomType(Enum):
    HALLWAY = "HallWay"
    ENGINEROOM = "EngineRoom"
    BRIDGE = "Bridge"
    MESSHALL = "MessHall"
    MEDBAY = "MedBay"

class Room():
    def __init__(self, roomtype):
        self.inventory = []
        self.spacemen = []
        self.aliens = []
        match roomtype:
            case RoomType.HALLWAY:
                self.type = RoomType.HALLWAY
                self.destinations = [ RoomType.BRIDGE, RoomType.ENGINEROOM, RoomType.MEDBAY, RoomType.MESSHALL, ]
            case RoomType.ENGINEROOM:
                self.type = RoomType.ENGINEROOM
                self.destinations = [ RoomType.HALLWAY ]
            case RoomType.BRIDGE:
                self.type = RoomType.BRIDGE
                self.destinations = [ RoomType.HALLWAY ]
            case RoomType.MESSHALL:
                self.type = RoomType.MESSHALL
                self.destinations = [ RoomType.MESSHALL ]
            case RoomType.MEDBAY:
                self.type = RoomType.MEDBAY
                self.destinations = [ RoomType.HALLWAY ]

    def take_turn(self, counter):
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
            for alien in self.aliens:
                alien.move()
        
        # grow, aliens only
        for alien in self.aliens:
            alien.grow(self)

    def addInventory(self, weapon):
        self.inventory.append(weapon)

    def removeInventory(self, weapon):
        self.inventory.remove(weapon)
