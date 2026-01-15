from Enum import Enum

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
            case HALLWAY:
                #build hallway
            case ENGINEROOM:
                #build engineroom
            case BRIDGE:
                # build bridge
            case MESSHALL:
                # build messhall
            case MEDBAY:
                # build medbay
