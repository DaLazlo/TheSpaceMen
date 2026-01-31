from enum import Enum


class RoomType(Enum):
    HALLWAY = "HallWay"
    ENGINEROOM = "Engine Room"
    BRIDGE = "Bridge"
    MESSHALL = "MessHall"
    MEDBAY = "MedBay"

class Room():
    destinations = []

    def __init__(self, roomtype: RoomType):
        self.inventory = []
        self.spacemen = []
        self.aliens = []
        self.destinations = []
        match roomtype:
            case RoomType.HALLWAY:
                self.type = RoomType.HALLWAY
                self.name = RoomType.HALLWAY.value

            case RoomType.ENGINEROOM:
                self.type = RoomType.ENGINEROOM
                self.name = RoomType.ENGINEROOM.value

            case RoomType.BRIDGE:
                self.type = RoomType.BRIDGE
                self.name = RoomType.BRIDGE.value

            case RoomType.MESSHALL:
                self.type = RoomType.MESSHALL
                self.name = RoomType.MESSHALL.value

            case RoomType.MEDBAY:
                self.type = RoomType.MEDBAY
                self.name = RoomType.MEDBAY.value

    def take_turn(self):
        #print(f"Room: {self.name}")
        # act, spacemen only
        for spaceman in self.spacemen:
            spaceman.act(self)

        # attack, spacemen first
        for spaceman in self.spacemen:
            if len(self.aliens) > 0:
                spaceman.attack(self.aliens[0], self)
                if self.aliens[0].stage == -1:
                    dead = self.aliens.pop()
                    print(f"{spaceman.name} killed {dead.name}")
        for alien in self.aliens:
            if len(self.spacemen) > 0:
                alien.attack(self.spacemen[0])
                if self.spacemen[0].health < 1:
                    dead = self.spacemen.pop()
                    print(f"{alien.name} killed {dead.name}")
        
        # move, only if no enemies present
        if len(self.aliens) == 0:
            for spaceman in self.spacemen:
                spaceman.move(self)
        elif len(self.spacemen) == 0:
            for alien in self.aliens:
                alien.move(self)
        
        # grow, aliens only
        for alien in self.aliens:
            alien.grow(self)

    def addInventory(self, weapon):
        self.inventory.append(weapon)

    def removeInventory(self, weapon):
        self.inventory.remove(weapon)
