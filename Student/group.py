from decorators import check_decorator

class Group:

    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []
        self.faculty = None
        self.group_leader = None

    def __repr__(self):
        return self.group_name

    def add_student(self, student):
        if student.faculty == self.faculty and not student.group:
            self.members.append(student)
            student.group = self
            return True
        return False

    @check_decorator
    def remove_student(self, student):
        self.members.remove(student)
        student.group = None
        return True

    @check_decorator
    def change_group_leader(self, student):
        self.group_leader = student
        return True
