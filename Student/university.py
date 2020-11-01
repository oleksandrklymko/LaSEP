class University:

    def __init__(self, title):
        self.title = title
        self.students = []
        self.faculties = []
        self.lecturers = []

    def __repr__(self):
        return self.title

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.university = self
            return True
        return False

    def add_lecturer(self, lecturer):
        if lecturer not in self.lecturers:
            self.lecturers.append(lecturer)
            lecturer.university = self
            return True
        return False

    def add_faculty(self, faculty):
        if faculty not in self.faculties:
            self.faculties.append(faculty)
            return True
        return False

    def show_information_about_student(self, student):
        if student in self.students:
            print(f'Student: {student}, rating: {student.rating}, stipend: {student.stipend}')
            return True
        return False

    def show_students_with_rating_from_x_to_y(self, x, y):
        students_in_rage = {}
        for student in self.students:
            if x >= student.rating >= y:
                students_in_rage[student] = student.rating

        students_in_rage = sorted(students_in_rage.items(), key=lambda x: x[1], reverse=True)
        for k, v in students_in_rage:
            print(k, v)

    def show_all_university_members(self):
        for faculty in self.faculties:
            print(faculty)
            for group in faculty.groups:
                print(group)
                for member in group.members:
                    if member == group.group_leader:
                        print(f'\t{member} - Group Leader')
                    else:
                        print(f'\t{member}')
