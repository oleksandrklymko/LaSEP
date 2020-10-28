class Lecturer:

    def __init__(self, first_name, last_name, subject_name):
        self.first_name = first_name
        self.last_name = last_name
        self.subject_name = subject_name

    def do_exam_for_group(self, group):
        for student in group.members:
            student.marks[self.subject_name] = 0

    def rate_student(self, student, rate):
        if self.subject_name in student.marks and rate in range(0, 6):
            student.marks[self.subject_name] = float(rate)
            student.rating = sum(student.marks.values()) / len(student.marks)
            if student.rating > 4:
                student.stipend = 1350
            elif student.rating > 3:
                student.stipend = 1100
            else:
                student.stipend = 0
            return True
        return False
