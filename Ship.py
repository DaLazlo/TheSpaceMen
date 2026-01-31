from random import randint, choice

from Room import *
from SpaceMan import *
from Alien import *
from Weapons import *
from Effect import *

class Ship():
    def __init__(self):
        self.rooms = {}

    def turn_zero(self):
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
            


    def setup(self, count):
        if count == 0:
            self.turn_zero()
        else:
            someplace = choice(list(RoomType))
            self.rooms[someplace].aliens.append(Alien(1))
            print(f"Spawned alien in {someplace}")

    def take_turn(self):
        for room in self.rooms.keys():
            self.rooms[room].take_turn()


        
