class Room:
    rooms = []

    def __init__(self, room_number):
        self.room_number = room_number
        self.members = []
        Room.rooms.append(self)

    def __repr__(self):
        return str(self.room_number)

    def settle(self, student):
        for i in range(len(Room.rooms)):
            if student in Room.rooms[i].members or len(self.members) >= 3:
                return False
        self.members.append(student)
        return True

    def evict(self, student):
        if student in self.members:
            self.members.remove(student)
            return True
        return False
