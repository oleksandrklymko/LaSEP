class Flight:
    flight_id = 1

    def __init__(self, departure, destination, departure_time, destination_time):
        self.flight_id = self.__class__.flight_id
        self.departure = departure
        self.destination = destination
        self.departure_time = departure_time
        self.destination_time = destination_time
        self.stewardesses = []
        self.permitted_models = []
        self.taken_places = 0
        self.plane = None
        self.captain = None
        self.pilot = None
        self.__class__.flight_id += 1

    def __repr__(self):
        return str(self.flight_id) + ' ' + self.departure + ' - ' + self.destination
