from Room import Room, RoomType

class Ship():
    def __init__(self):
        self.Hallway = Room(RoomType.HALLWAY)
        self.EngineRoom = Room(RoomType.ENGINEROOM)
        self.Bridge = Room(RoomType.BRIDGE)
        self.MessHall = Room(RoomType.MESSHALL)
        self.MedBay = Room(RoomType.MEDBAY)

    def take_turn(self):
        pass
