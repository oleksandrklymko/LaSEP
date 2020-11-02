class Faculty:

    def __init__(self, title):
        self.title = title
        self.groups = []

    def __repr__(self):
        return self.title

    def add_student(self, student):
        if student.faculty:
            return False
        student.faculty = self
        return True

    def add_group(self, group):
        if group not in self.groups:
            self.groups.append(group)
            group.faculty = self
            return True
        return False

    def rate_students(self, group):
        if group in self.groups:
            for student in group.members:
                student.rating = sum(student.marks.values()) / len(student.marks)

    def calculate_stipend(self):
        for group in self.groups:
            for student in group.members:
                if student.rating > 4:
                    student.stipend = 1350
                elif student.rating > 3:
                    student.stipend = 1100
                else:
                    student.stipend = 0
            return True
        return False
