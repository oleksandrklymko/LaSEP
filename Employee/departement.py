from datetime import datetime, timedelta


class Department:

    def __init__(self, title, title_abbreviation):
        self.title = title
        self.title_abbreviation = title_abbreviation
        self.members = []
        self.members_on_vacation = []
        self.leader = None
        self.enterprise = None

    def __repr__(self):
        return self.title

    def __check_if_employee_in_members(self, employee):
        return employee in self.members

    def add_employee(self, employee):
        for department in self.enterprise.departments:
            if employee.enterprise != self.enterprise or employee in department.members or len(self.members) >= 20:
                return False
        self.members.append(employee)
        employee.department = self
        return True

    def remove_employee(self, employee):
        if self.__check_if_employee_in_members(employee):
            self.members.remove(employee)
            employee.department = None
            if self.leader == employee:
                self.leader = None
            return True
        return False

    def change_leader(self, employee):
        if self.__check_if_employee_in_members(employee):
            self.leader = employee
            return True
        return False

    def increase_employee_salary(self, employee, percent=1.2):
        if self.__check_if_employee_in_members(employee):
            if datetime.date(datetime.today()) >= employee.job_start_date + timedelta(365):
                employee.salary += (employee.salary * percent / 100)
                return True
        return False

    def show_information_about_vacations(self):
        for employee in self.members:
            if employee.vacations:
                days_in_vacation = employee.current_job.vacation_days - employee.vacation_days
                print(f'{employee} , days in vacation - {days_in_vacation}: ')
                for start_date, end_date in employee.vacations:
                    print(f'\tFrom {start_date} to {end_date}')
