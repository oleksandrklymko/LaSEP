
from datetime import datetime


class Student:
    students = []

    def __init__(self, first_name, last_name, patronymic, year_of_birth, place_of_birth, sex, marital_status):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.year_of_birth = year_of_birth
        self.place_of_birth = place_of_birth
        self.sex = sex
        self.marital_status = marital_status
        self.rented_books = []
        self.room_number = None
        self.group = None
        self.marks = {}
        self.rating = 0
        self.credit = 0
        self.campus_card = len(Student.students) + 1
        Student.students.append(self)

    def __repr__(self):
        return self.first_name + ' ' + self.last_name

    @classmethod
    def show_students_with_rating_from_x_to_y(cls, x, y):
        students_in_rage = {}
        for student in cls.students:
            if x >= student.rating >= y:
                students_in_rage[student] = student.rating

        students_in_rage = sorted(students_in_rage.items(), key=lambda x: x[1], reverse=True)
        for k, v in students_in_rage:
            print(k, v)
