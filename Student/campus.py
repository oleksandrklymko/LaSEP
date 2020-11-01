class Campus:

    def __init__(self, title):
        self.title = title
        self.rooms = []

    def __repr__(self):
        return self.title

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)
            room.campus = self
            return True
        return False
