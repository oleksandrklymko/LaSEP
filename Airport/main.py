from airport import Airport
from captain import Captain
from employee import Employee
from customer import Customer
from flight import Flight
from model import Model
from pilot import Pilot
from plane import Plain
from stewardess import Stewardess
from datetime import datetime

airport = Airport('Lviv')
alex = Pilot('Klymko', '14.08.99', 'Lviv', 'III')
nazar = Customer('Nazar', 'Anisiimov')
model1 = Model('Trasport', 50, 500000)
plane1 = Plain(484, model1)
captain1 = Captain('Rox', '14.41241', 'Zhovkva')
stewardess1 = Stewardess('Anisimova', '202020', 'Zhovkva')
stewardess2 = Stewardess('Klymko', '202020', 'Zhovkva')

kyivlviv = Flight('Lviv', 'Kyiv', datetime(2020, 11, 5, 14, 30), datetime(2020, 11, 6, 14, 30))

airport.add_employee(alex)
airport.add_employee(captain1)
airport.add_employee(stewardess1)

airport.add_employee(stewardess2)
airport.add_plain(plane1)
airport.add_flight(kyivlviv)
airport.permit_model_to_flight(kyivlviv, model1)
airport.add_plane_to_flight(plane1, kyivlviv)
airport.add_permission_to_fly_on_plane(alex, plane1)
airport.add_pilot_to_flight(alex, kyivlviv)
airport.show_all_pilots_for_model(model1)
airport.add_captain_to_flight(captain1, kyivlviv)
nazar.buy_ticket_for_a_flight(airport, kyivlviv, 26)

airport.add_stewardess_to_flight(stewardess1, kyivlviv)
airport.add_stewardess_to_flight(stewardess2, kyivlviv)
airport.start_a_flight(kyivlviv)
print(airport.history_of_flights)

airport.show_info_about_successful_flights()


