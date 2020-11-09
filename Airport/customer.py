class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.bought_tickets = {}

    def __repr__(self):
        return self.first_name + ' ' + self.last_name

    def buy_ticket_for_a_flight(self, airport, flight, quantity):
        if flight in airport.flights:
            if flight.taken_places < flight.plane.model.places:
                flight.taken_places += quantity
                self.bought_tickets[flight.flight_id] = quantity
                airport.add_tickets_to_bought_list(flight, quantity)
                return True
            return False
        return False
