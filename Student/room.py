class Room:

    def __init__(self, room_number):
        self.room_number = room_number
        self.members = []
        self.campus = None

    def __repr__(self):
        return 'Room №' + str(self.room_number)

    def settle(self, student):
        for room in self.campus.rooms:
            if student in room.members:
                return False
        if len(self.members) < 3:
            self.members.append(student)
            student.room_number = self
            return True
        return False

    def evict(self, student):
        if student in self.members:
            self.members.remove(student)
            student.room_number = None
            return True
        return False
