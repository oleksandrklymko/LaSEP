class Group:
    groups = []

    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []
        self.group_leader = None
        Group.groups.append(self)

    def __repr__(self):
        return self.group_name

    def add_student(self, student):
        for i in range(len(Group.groups)):
            if student in Group.groups[i].members:
                return False
        self.members.append(student)
        student.group = self.group_name
        return True

    def remove_student(self, student):
        if student in self.members:
            self.members.remove(student)
            return True
        return False

    def change_group_leader(self, student):
        if student in self.members:
            self.group_leader = student
            return True
        return False

    @classmethod
    def show_all_groups_members(cls):
        for group in cls.groups:
            print(group)
            for member in group.members:
                if member == group.group_leader:
                    print(f'\t{member} - Group Leader')
                else:
                    print(f'\t{member}')
