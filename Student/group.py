class Group:

    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []
        self.faculty = None
        self.group_leader = None

    def __repr__(self):
        return self.group_name

    def check_if_student_in_group(self, student):
        return student in self.members

    def add_student(self, student):
        if student.faculty == self.faculty and not student.group:
            self.members.append(student)
            student.group = self
            return True
        return False

    def remove_student(self, student):
        if self.check_if_student_in_group(student):
            self.members.remove(student)
            student.group = None
            return True
        return False

    def change_group_leader(self, student):
        if self.check_if_student_in_group(student):
            self.group_leader = student
            return True
        return False
