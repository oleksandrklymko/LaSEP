class Enterprise:
    def __init__(self, title):
        self.title = title
        self.departments = []
        self.employees = []
        self.jobs = []

    def __repr__(self):
        return self.title

    def __check_if_department_already_added(self, department):
        return department in self.departments

    def add_department(self, department):
        if self.__check_if_department_already_added(department):
            return False
        self.departments.append(department)
        department.enterprise = self
        return True

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            employee.enterprise = self
            return True
        return False

    def add_job_position(self, job):
        if job not in self.jobs:
            self.jobs.append(job)
            return True
        return False

    def show_information_about_departments(self):
        for department in self.departments:
            print(f'Leader: {department.leader}, total amount of employees: {len(department.members)}')

    def show_department_employees(self, department):
        if self.__check_if_department_already_added(department):
            print(f'{department} employees:')
            for employee in department.members:
                print(f'\t{employee}')
        return False
