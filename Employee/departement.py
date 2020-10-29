class Department:
    departments = []

    def __init__(self, title, title_abbreviation):
        self.title = title
        self.title_abbreviation = title_abbreviation
        self.members = []
        self.members_on_vacation = []
        self.leader = None
        Department.departments.append(self)

    def __repr__(self):
        return self.title

    def add_employee(self, employee):
        for i in range(len(Department.departments)):
            if employee in Department.departments[i].members or len(self.members) >= 20:
                return False
            self.members.append(employee)
            employee.department = self
            return True

    def remove_employee(self, employee):
        if employee in self.members:
            self.members.remove(employee)
            employee.department = None
            if self.leader == employee:
                self.leader = None
            return True
        return False

    def change_leader(self, employee):
        if employee in self.members:
            self.leader = employee
            return True
        return False

    @classmethod
    def show_information_about_departments(cls):
        for department in Department.departments:
            print(f'Leader: {department.leader}, total amount of employees: {len(department.members)}')


def show_department_employees(department):
    if department in Department.departments:
        print(f'{department}:')
        for member in department.members:
            print(f'\t{member}')
