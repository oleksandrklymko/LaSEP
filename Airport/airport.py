from stewardess import Stewardess
from pilot import Pilot
from captain import Captain
from datetime import datetime, timedelta


class Airport:

    def __init__(self, title):
        self.title = title
        self.flights = []
        self.aircrafts = []
        self.captains = []
        self.pilots = []
        self.available_employees = []
        self.stewardesses = []
        self.currently_on_flight = []
        self.sold_tickets = {}
        self.history_of_flights = {}

    def __repr__(self):
        return self.title

    def add_employee(self, employee):
        if isinstance(employee, Pilot):
            self.pilots.append(employee)
            self.available_employees.append(employee)
            return True
        elif isinstance(employee, Captain):
            self.captains.append(employee)
            self.available_employees.append(employee)
            return True
        elif isinstance(employee, Stewardess):
            self.stewardesses.append(employee)
            self.available_employees.append(employee)
            return True
        return False

    def add_tickets_to_bought_list(self, flight, quantity):
        if flight in self.sold_tickets:
            self.sold_tickets[flight] += quantity
            return True
        self.sold_tickets[flight] = quantity

    def start_a_flight(self, flight, stewardesses_number=2):
        crew_is_full = flight.plane and flight.pilot and len(flight.stewardesses) == stewardesses_number
        more_then_half_places_sold = flight.taken_places > flight.plane.model.places/2
        if flight.pilot.last_flight:
            pilot_have_3_days_delay = datetime.now() > flight.pilot.last_flight + timedelta(3)
        else:
            pilot_have_3_days_delay = True
        if crew_is_full and more_then_half_places_sold and pilot_have_3_days_delay:
            flight.pilot.last_flight = flight.departure
            self.history_of_flights[flight] = flight.taken_places
            self.currently_on_flight.append(flight.pilot)
            self.currently_on_flight.append(flight.captain)
            for member in self.stewardesses:
                self.currently_on_flight.append(member)
            duration = flight.destination_time - flight.departure_time
            days, seconds = duration.days, duration.seconds
            hours = days * 24 + seconds // 3600
            flight.plane.hours_worked += hours
            return True
        else:
            return False

    def add_plain(self, plain):
        if plain not in self.aircrafts:
            self.aircrafts.append(plain)
            return True
        return False

    def add_flight(self, flight):
        if flight not in self.flights:
            self.flights.append(flight)
            return True
        return False

    def add_permission_to_fly_on_plane(self, pilot, plain):
        if pilot in self.pilots and plain in self.aircrafts:
            pilot.allowed_types.append(plain)
            return True
        return False

    def permit_model_to_flight(self, flight, model):
        if flight in self.flights and model not in flight.permitted_models:
            flight.permitted_models.append(model)
            return True
        return False

    def add_plane_to_flight(self, plane, flight):
        if flight in self.flights and plane.model in flight.permitted_models:
            flight.plane = plane
            return True
        return False

    def add_pilot_to_flight(self, pilot, flight):
        if pilot in self.pilots and not self.currently_on_flight and flight.plane in pilot.allowed_types:
            flight.pilot = pilot
            self.currently_on_flight.append(pilot)
            return True
        return False

    def add_captain_to_flight(self, captain, flight):
        if captain in self.captains and captain not in self.currently_on_flight:
            flight.captain = captain
            return True
        return False

    def add_stewardess_to_flight(self, stewardess, flight):
        if stewardess in self.stewardesses and stewardess not in self.currently_on_flight and len(flight.stewardesses) < 2:
            flight.stewardesses.append(stewardess)
            return True
        return False

    def show_all_pilots_for_model(self, model):
        for plain in self.aircrafts:
            print(plain)
            for pilot in self.pilots:
                if plain.model == model and plain in pilot.allowed_types:
                    print('\t', pilot, pilot.rank)

    def show_info_about_successful_flights(self):
        for flight in self.history_of_flights:
            print(flight.departure_time.date(), flight.flight_id, flight.plane, flight.plane.model, flight.taken_places)

    def show_all_stewardesses(self):
        for stewardess in self.stewardesses:
            print(stewardess, stewardess.sname, stewardess.address, stewardess.employee_id)