class Room:
    rooms = []

    def __init__(self, room_number):
        self.room_number = room_number
        self.members = []
        Room.rooms.append(self)

    def __repr__(self):
        return str(self.room_number)

    def settle_in_a_room(self, student):
        if len(self.members) >= 3:
            return False
        else:
            student.room_number = self.room_number
            self.members.append(student)
            return True

    def evict_from_the_room(self, student):
        if student in self.members:
            self.members.remove(student)
            return True
        return False
