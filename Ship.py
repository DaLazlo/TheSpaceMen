from random import randint, choice

from Room import *
from SpaceMan import *
from Alien import *
from Weapons import *
from Effect import *

class Ship():
    def __init__(self):
        self.rooms = {}

    def setup(self):
        for room in RoomType:
            self.rooms[RoomType.HALLWAY] = Room(RoomType.HALLWAY)
            self.rooms[RoomType.BRIDGE] = Room(RoomType.BRIDGE)
            self.rooms[RoomType.ENGINEROOM] = Room(RoomType.ENGINEROOM)
            self.rooms[RoomType.MEDBAY] = Room(RoomType.MEDBAY)
            self.rooms[RoomType.MESSHALL] = Room(RoomType.MESSHALL)
        
        self.rooms[RoomType.HALLWAY].destinations = [   self.rooms[RoomType.BRIDGE], 
                                                        self.rooms[RoomType.ENGINEROOM], 
                                                        self.rooms[RoomType.MEDBAY], 
                                                        self.rooms[RoomType.MESSHALL] ]
        self.rooms[RoomType.BRIDGE].destinations = [    self.rooms[RoomType.HALLWAY] ]
        self.rooms[RoomType.ENGINEROOM].destinations = [    self.rooms[RoomType.HALLWAY] ]
        self.rooms[RoomType.MEDBAY].destinations = [    self.rooms[RoomType.HALLWAY] ]
        self.rooms[RoomType.MESSHALL].destinations = [    self.rooms[RoomType.HALLWAY] ]

        for room in self.rooms.keys():
            match (room):
                case RoomType.BRIDGE:
                    self.rooms[room].spacemen.append(SpaceMan(Crew.CAPTAIN))
                    print(f"{Crew.CAPTAIN.value} starts on {room.value}")
                    self.rooms[room].inventory.append(Weapon(WeaponType.PISTOL))
                    print(f"{WeaponType.PISTOL.value} starts on {room.value}")
                case RoomType.ENGINEROOM:
                    self.rooms[room].spacemen.append(SpaceMan(Crew.ENGINEER))
                    print(f"{Crew.ENGINEER.value} starts on {room.value}")
                    self.rooms[room].inventory.append(Weapon(WeaponType.EXTINGUISHER))
                    print(f"{WeaponType.EXTINGUISHER.value} starts on {room.value}")
                case RoomType.MEDBAY:
                    self.rooms[room].spacemen.append(SpaceMan(Crew.MEDIC))
                    print(f"{Crew.MEDIC.value} starts on {room.value}")
                    self.rooms[room].inventory.append(Weapon(WeaponType.SYRINGE))
                    print(f"{WeaponType.SYRINGE.value} starts on {room.value}")
                case RoomType.MESSHALL:
                    self.rooms[room].spacemen.append(SpaceMan(Crew.COOK))
                    print(f"{Crew.COOK.value} starts on {room.value}")
                    self.rooms[room].inventory.append(Weapon(WeaponType.CLEAVER))
                    print(f"{WeaponType.CLEAVER.value} starts on {room.value}")
                case RoomType.HALLWAY:
                    print(f"{room.value} is clear, for now...")

        for i in range(0,5):
            someplace = choice(list(RoomType))
            self.rooms[someplace].aliens.append(Alien(1))
            print(f"Spawned Alien  {i} in {someplace.value}")

    def take_turn(self):
        aliens = 0
        spacemen = 0
        for room in self.rooms.keys():
            self.rooms[room].take_turn()
            aliens += len(self.rooms[room].aliens)
            spacemen += len(self.rooms[room].spacemen)
        print(f"Spacemen: {spacemen}   Aliens: {aliens}")
        if spacemen < 1 or aliens < 1:
            return True
        else:
            return False


        
