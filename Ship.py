from random import randint

from Room import *
from SpaceMan import *
from Alien import *
from Weapons import *
from Effect import *

class Ship():
    def __init__(self):
        self.rooms = []
        self.rooms.append(Room(RoomType.HALLWAY))
        self.rooms.append(Room(RoomType.ENGINEROOM))
        self.rooms.append(Room(RoomType.BRIDGE))
        self.rooms.append(Room(RoomType.MESSHALL))
        self.rooms.append(Room(RoomType.MEDBAY))

    def turn_zero(self):
        for room in self.rooms:
            match (room.type):
                case RoomType.BRIDGE:
                    room.spacemen.append(SpaceMan(Crew.CAPTAIN))
                    room.addInventory(Weapon(WeaponType.PISTOL))
                case RoomType.ENGINEROOM:
                    room.spacemen.append(SpaceMan(Crew.ENGINEER))
                    room.addInventory(Weapon(WeaponType.EXTINGUISHER))
                case RoomType.MEDBAY:
                    room.spacemen.append(SpaceMan(Crew.MEDIC))
                    room.addInventory(Weapon(WeaponType.SYRINGE))
                case RoomType.MESSHALL:
                    room.spacemen.append(SpaceMan(Crew.COOK))
                    room.addInventory(Weapon(WeaponType.CLEAVER))

    def setup(self, count):
        if count == 0:
            turn_zero()
        else:
            match(randint(0, len(self.rooms)-1)):
                case 0:
                    self.rooms[0].aliens.append(Alien(1))
                    print(f"Spawned alien in {self.rooms[0].name}")

    def take_turn(self):
        for room in self.rooms:
            room.take_turn()


        
