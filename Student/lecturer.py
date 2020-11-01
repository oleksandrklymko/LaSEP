class Lecturer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.university = None
        self.subjects = []

    def check_if_subject_in_subjects(self, subject):
        return subject in self.subjects

    def add_subject(self, subject):
        if self.check_if_subject_in_subjects(subject):
            return False
        self.subjects.append(subject)
        return True

    def do_exam_for_group(self, subject, group):
        if self.check_if_subject_in_subjects(subject):
            for student in group.members:
                student.marks[subject] = 0
            return True
        return False

    def grade_student(self, subject, student, grade):
        if self.check_if_subject_in_subjects(subject) and subject in student.marks and grade in range(0, 6):
            student.marks[subject] = float(grade)
            return True
        return False
