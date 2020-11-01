# Предметна область “Студент”.

# Кожен студент характеризується такими атрибутами : прізвище, імя, по  батькові, номер студентського квитка, рік народження,
# місце народження, адреса, стать, сімейний стан, стипендія, кімната в гуртожитку. В одній кімнати проживає до трьох студентів.
# Кожен студент вчиться в певній групі, яка має свого старосту, та разом з іншими студентами групи вчить та здає певні предмети у
# певних викладачів, при цьому отримуючи деяку суму балів та державну оцінку. Студент може мати деякі захоплення (хоббі).
# Студенти відвідують бібліотеку де можна позичити книжку, що характеризується номером, автором, назвою, жанром.
# Кожна книжка не може бути одночасно видана двом студентам. Студент не може мати одночасно позиченими книжок на суму більше ніж 100 крб.
# Стипендія нараховується згідно з рейтингом за певною процедурою.

# Система повинна видавати звіти:
# Cписок студентів по групах,
# Cписок студентів які мають рейтинг від X до Y,
# Cписок студентів та книг що не повернені більше року (з підсумовуванням кількості книг та грошового боргу студента),
# Довідка для студента про його рейтинг та розмір стипендії


from university import University
from faculty import Faculty
from group import Group
from campus import Campus
from student import Student
from room import Room
from lecturer import Lecturer
from subject import Subject
from book import Book
from library import Library

from datetime import date

nulp = University('NU LP')

computer_science = Faculty('Computer Science')

kn41z = Group('kn-41z')
kn42z = Group('kn-42z')

campus = Campus('NU LP CAMPUS №1')

alex = Student('Oleksandr', 'Klymko', 'Vasylovich', 1999, 'Zhovkva', 'Male')
oleksii = Student('Oleksii', 'Khomyn', 'Petrovich', 1998, 'Lviv', 'Male')
rostyk = Student('Rostystav', 'Koretskiy', 'Yaroslavovich', 1999, 'Horodenka', 'Male')
maskim = Student('Maksim', 'Nimko', 'Ihorovich', 2002, 'Striy', 'Male')
igor = Student('Igor', 'Hamaliy', 'Petrovich', 1998, 'Lviv', 'Male')
ostap = Student('Ostap', 'Mazur', 'Bogdanovich', 1999, 'Sambir', 'Male')
oleg = Student('Oleg', 'Novosad', 'Igorovich', 1998, 'Lviv', 'Male')
nazar = Student('Nazar', 'Anisimov', 'Yaroslavovich', 1999, 'Striy', 'Male')
anton = Student('Anton', 'Lunenko', 'Vasylovich', 2001, 'Kyiv', 'Male')
artem = Student('Artem', 'Vasylushin', 'Romanovich', 2000, 'Rava-Ruska', 'Male')

room1 = Room(1)
room2 = Room(2)
room3 = Room(3)
room4 = Room(4)
room5 = Room(5)

ivanna_dorosh = Lecturer('Orysa', 'Dorosh')
bogdan_mazur = Lecturer('Bogdan', 'Mazur')
natalia_bokla = Lecturer('Natalia', 'Bokla')

web_design = Subject('Web Design')
math = Subject('Math')
algorithms = Subject('Algorithms')

book1 = Book('M. Lutz', 'Learning Python3', 'tech', 30)
book2 = Book('A. Sapkowski', 'Witcher', 'fantasy', 20)
book3 = Book('Emily St. John Mandel', 'The Glass Hotel', 'post-apocalyptic novel', 20)
book4 = Book('Yuval Noah Harari', 'Sapiens: A Brief History of Humankind', 'history', 90)
book5 = Book('Stephen Hawking', 'A Brief History of Time', 'science', 50)


library = Library()

nulp.add_student(alex)
nulp.add_student(oleksii)
nulp.add_student(rostyk)
nulp.add_student(maskim)
nulp.add_student(igor)
nulp.add_student(ostap)
nulp.add_student(oleg)
nulp.add_student(nazar)
nulp.add_student(anton)
nulp.add_student(artem)

nulp.add_faculty(computer_science)

computer_science.add_student(alex)
computer_science.add_student(oleksii)
computer_science.add_student(rostyk)
computer_science.add_student(maskim)
computer_science.add_student(ostap)
computer_science.add_student(oleg)
computer_science.add_student(nazar)
computer_science.add_student(anton)
computer_science.add_student(artem)

computer_science.add_group(kn41z)
computer_science.add_group(kn42z)

kn41z.add_student(alex)
kn41z.add_student(oleksii)
kn41z.add_student(rostyk)
kn41z.add_student(maskim)
kn42z.add_student(ostap)
kn42z.add_student(oleg)
kn42z.add_student(nazar)
kn42z.add_student(anton)
kn42z.add_student(artem)

kn41z.change_group_leader(rostyk)
kn42z.change_group_leader(anton)


campus.add_room(room1)
campus.add_room(room2)
campus.add_room(room3)
campus.add_room(room4)
campus.add_room(room5)

room1.settle(alex)
room1.settle(oleksii)
room1.settle(rostyk)
room1.settle(maskim)

room2.settle(maskim)
room2.settle(ostap)
room2.settle(oleg)

room4.settle(nazar)

room5.settle(artem)
room5.settle(anton)

ivanna_dorosh.add_subject(web_design)
natalia_bokla.add_subject(math)
ivanna_dorosh.add_subject(algorithms)

ivanna_dorosh.do_exam_for_group(algorithms, kn42z)
ivanna_dorosh.do_exam_for_group(web_design, kn42z)

ivanna_dorosh.grade_student(algorithms, artem, 5)
ivanna_dorosh.grade_student(algorithms, ostap, 3)
ivanna_dorosh.grade_student(algorithms, oleg, 2)
ivanna_dorosh.grade_student(algorithms, nazar, 3)
ivanna_dorosh.grade_student(algorithms, anton, 4)
ivanna_dorosh.grade_student(algorithms, artem, 5)

ivanna_dorosh.grade_student(web_design, artem, 1)
ivanna_dorosh.grade_student(web_design, ostap, 5)
ivanna_dorosh.grade_student(web_design, oleg, 5)
ivanna_dorosh.grade_student(web_design, nazar, 4)
ivanna_dorosh.grade_student(web_design, anton, 2)
ivanna_dorosh.grade_student(web_design, artem, 5)

computer_science.rate_students(kn42z)


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

library.borrow_book(book1, alex, date(2018, 8, 14))
library.borrow_book(book2, ostap, date(2020, 8, 20))

library.show_all_debtors()

computer_science.calculate_stipend()

nulp.show_all_university_members()
