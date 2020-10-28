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


from datetime import date

from student import Student
from group import Group
from room import Room
from lecturer import Lecturer
from book import Book
from library import Library

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


kn41z = Group('kn-41z')
kn42z = Group('kn-42z')
kn43z = Group('kn-43z')

room1 = Room(1)
room2 = Room(2)
room3 = Room(3)
room4 = Room(4)
room5 = Room(5)

ivanna_dorosh = Lecturer('Orysa', 'Dorosh', 'Probability theory')
bogdan_mazur = Lecturer('Bogdan', 'Mazur', 'Programming on Assembly')
natalia_bokla = Lecturer('Natalia', 'Bokla', 'Creating web apllication')


book1 = Book('M. Lutz', 'Learning Python3', 'tech', 30)
book2 = Book('A. Sapkowski', 'Witcher', 'fantasy', 20)
book3 = Book('Emily St. John Mandel', 'The Glass Hotel', 'post-apocalyptic novel', 20)
book4 = Book('Yuval Noah Harari', 'Sapiens: A Brief History of Humankind', 'history', 90)
book5 = Book('Stephen Hawking', 'A Brief History of Time', 'science', 50)


library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

room4.settle(alex)
room4.settle(rostyk)
room4.settle(oleksii)
room4.settle(artem)

room2.settle(maskim)
room2.settle(ostap)
room2.settle(alex)
room2.settle(artem)

room1.settle(anton)
room1.settle(nazar)
room1.settle(oleg)

room3.settle(igor)

room2.evict(maskim)
room3.settle(maskim)

room1.evict(igor)


kn41z.add_student(maskim)
kn41z.add_student(anton)
kn41z.add_student(artem)
kn41z.add_student(ostap)
kn41z.change_group_leader(maskim)


kn42z.add_student(alex)
kn42z.add_student(oleksii)
kn42z.add_student(rostyk)
kn42z.add_student(maskim)
kn42z.add_student(igor)
kn42z.change_group_leader(maskim)
kn42z.change_group_leader(alex)


kn43z.add_student(nazar)
kn43z.add_student(oleg)
kn43z.change_group_leader(nazar)

Group.show_all_groups_members()

natalia_bokla.do_exam_for_group(kn42z)
natalia_bokla.rate_student(alex, 4)
natalia_bokla.rate_student(rostyk, 5)
natalia_bokla.rate_student(igor, 3)
natalia_bokla.rate_student(oleksii, 4)

ivanna_dorosh.do_exam_for_group(kn42z)
ivanna_dorosh.do_exam_for_group(kn41z)

ivanna_dorosh.rate_student(alex, 3)
ivanna_dorosh.rate_student(rostyk, 4)
ivanna_dorosh.rate_student(igor, 5)
ivanna_dorosh.rate_student(oleksii, 2)

ivanna_dorosh.rate_student(maskim, 5)
ivanna_dorosh.rate_student(anton, 4)
ivanna_dorosh.rate_student(ostap, 3)
ivanna_dorosh.rate_student(artem, 4)

Student.show_students_with_rating_from_x_to_y(5,4)

library.borrow_book(book1, alex, date(2015, 5, 14))
library.borrow_book(book1, rostyk, date(2019, 3, 1))
library.borrow_book(book3, maskim)
library.borrow_book(book2, ostap, date(2017, 4, 20))
library.borrow_book(book4, alex)


library.show_all_debtors()

alex.show_information()
maskim.show_information()
