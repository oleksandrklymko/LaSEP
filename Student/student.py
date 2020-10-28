class Student:
    students = []

    def __init__(self, first_name, last_name, patronymic, year_of_birth, place_of_birth, sex, marital_status=None):
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
        self.hobbies = []
        self.marks = {}
        self.rating = 0
        self.credit = 0
        self.stipend = 0
        self.campus_card = len(Student.students) + 1
        Student.students.append(self)

    def __repr__(self):
        return self.first_name + ' ' + self.last_name

    def show_information(self):
        print(f'Student: {self}, rating: {self.rating}, stipend: {self.stipend}')

    def add_hobby(self, hobby):
        if hobby not in self.hobbies:
            self.hobbies.append(hobby)
            return True
        return False

    @classmethod
    def show_students_with_rating_from_x_to_y(cls, x, y):
        students_in_rage = {}
        for student in cls.students:
            if x >= student.rating >= y:
                students_in_rage[student] = student.rating

        students_in_rage = sorted(students_in_rage.items(), key=lambda x: x[1], reverse=True)
        for k, v in students_in_rage:
            print(k, v)


if __name__ == '__main__':
    alex = Student('Oleksandr', 'Klymko', 'Vasylovich', 1999, 'Zhovkva', 'Male')
    oleksii = Student('Oleksii', 'Khomyn', 'Petrovich', 1988, 'Lviv', 'Male')
    rostyk = Student('Rostystav', 'Koretskiy', 'Yaroslavovich', 1999, 'Horodenka', 'Male')
    maskim = Student('Maksim', 'Nimko', 'Ihorovich', 2002, 'Striy', 'Male')
    igor = Student('Igor', 'Hamaliy', 'Petrovich', 1998, 'Lviv', 'Male')

    oleksii.rating = 4.5
    rostyk.rating = 4.5
    maskim.rating = 3.5
    igor.rating = 3

    oleksii.show_information()

    oleksii.add_hobby('Boxing')
    print(oleksii.hobbies)

    print(igor.campus_card)

    Student.show_students_with_rating_from_x_to_y(4.5, 3)
