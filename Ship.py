from Room import Room, RoomType

class Ship():
    self.rooms = []
    def __init__(self):
        self.rooms.append(Room(RoomType.HALLWAY))
        self.rooms.append(Room(RoomType.ENGINEROOM))
        self.rooms.append(Room(RoomType.BRIDGE))
        self.rooms.append(Room(RoomType.MESSHALL))
        self.rooms.append(Room(RoomType.MEDBAY))

    def take_turn(self):
        for room in self.rooms:
            room.take_turn()
    
        
