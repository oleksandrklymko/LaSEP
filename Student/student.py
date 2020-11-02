class Student:
    campus_card_id = 1

    def __init__(self, first_name, last_name, patronymic, year_of_birth, place_of_birth, sex, marital_status=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.year_of_birth = year_of_birth
        self.place_of_birth = place_of_birth
        self.sex = sex
        self.marital_status = marital_status
        self.university = None
        self.faculty = None
        self.room_number = None
        self.group = None
        self.rented_books = []
        self.hobbies = []
        self.marks = {}
        self.rating = 0
        self.credit = 0
        self.stipend = 0
        self.campus_card = self.__class__.campus_card_id
        self.__class__.campus_card_id += 1

    def __repr__(self):
        return self.first_name + ' ' + self.last_name

    def add_hobby(self, hobby):
        if hobby not in self.hobbies:
            self.hobbies.append(hobby)
            return True
        return False
