from employee import Employee


class Pilot(Employee):
    def __init__(self, sname, date_of_birthday, address, rank):
        super().__init__(sname, date_of_birthday, address)
        self.rank = rank
        self.allowed_types = []
        self.last_flight = None
