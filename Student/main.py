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
from book import Book
from room import Room
from library import Library
from group import Group
from lecturer import Lecturer

alex = Student('Alex', 'Klymko', 'Vasylovich', 1999, 'Zhovkva', 'Male', 'In relationship')
alex2 = Student('Bohdan', 'Klymko', 'Vasylovich', 1999, 'Zhovkva', 'Male', 'relationship')
oleksii = Student('Oleksii','Khomyn', 'Petrovich', 1999, 'Lviv', 'Male', 'Single')


ivan = Lecturer('Ivan', 'Omelan', 'Web design')
oleh = Lecturer('Oleh', 'Kozak', 'IT technologies')

book1 = Book('Lutz', 'How to Learn Python', 'tech', 120)
book2 = Book('Brown', 'How to think like and CS', 'tech', 50)
book3 = Book('Martin', 'ASdsad', 'tech', 10)
book4 = Book('Anton', 'dsada to Learn Python', 'tech', 120)
book5 = Book('Boris', 'Hodsw to Learn Python', 'tech', 50)
book6 = Book('Hella', 'dsdsds to Learn Python', 'tech', 10)
book7 = Book('Adam', 'Meh to Learn Python', 'tech', 80)
book8 = Book('Sara', 'Pyro to Learn Python', 'tech', 90)

library = Library()
library.borrow_book(book2, alex)
library.show_all_debtors()



