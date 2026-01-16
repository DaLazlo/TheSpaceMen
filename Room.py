from enum import Enum

from Weapons import *

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
                #build hallway
                pass
            case RoomType.ENGINEROOM:
                #build engineroom
                pass
            case RoomType.BRIDGE:
                # build bridge
                pass
            case RoomType.MESSHALL:
                # build messhall
                pass
            case RoomType.MEDBAY:
                # build medbay
                pass

    def take_turn(self):
        pass
