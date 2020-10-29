from datetime import datetime, timedelta
from job_position import Job


class Employee:
    employees = []

    def __init__(self, first_name, last_name, patronymic, age, date_of_birth, place_of_birth, home_adress):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.age = age
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.current_job_position = None
        self.date_of_starting_current_job_position = None
        self.department = None
        self.salary = None
        self.job_positions = []
        self.vacations = []
        self.vacation_days = 0
        self.id = len(Employee.employees) + 1
        Employee.employees.append(self)

    def __repr__(self):
        return self.first_name + ' ' + self.last_name

    def change_job_position(self, job_position, starting_date=datetime.date(datetime.today())):
        if job_position in Job.jobs and self.current_job_position != job_position:
            if self.current_job_position:
                self.job_positions.append(self.current_job_position)
            self.date_of_starting_current_job_position = starting_date
            self.current_job_position = job_position
            self.salary = job_position.starting_salary
            self.vacation_days = job_position.vacation_days
            return True
        return False

    def increase_salary(self):
        if datetime.date(datetime.today()) >= self.date_of_starting_current_job_position + timedelta(365):
            self.salary = (self.salary * 1.2 / 100) + self.salary
            return True
        return False

    def take_vacation(self, end, begin=datetime.date(datetime.today())):
        days = int(str(end - begin).split(' ')[0])
        members_on_vacation = self.department.members_on_vacation
        if not self.department or days > self.vacation_days or self in members_on_vacation or len(
                members_on_vacation) >= 5:
            return False
        self.vacations.append((str(begin), str(end)))
        members_on_vacation.append(self)
        self.vacation_days -= days
        return True

    def return_from_vacation(self):
        if self in self.department.members_on_vacation:
            self.department.members_on_vacation.remove(self)
            return True
        return False

    def show_information(self):
        print(f'Current job position: \'{self.current_job_position}\', salary : {self.salary}')

    @classmethod
    def show_information_about_vacations(cls):
        for employee in Employee.employees:
            if employee.vacations:
                vacation_days_for_position = employee.current_job_position.vacation_days
                print(f'{employee} , days in vacation - {vacation_days_for_position - employee.vacation_days}: ')
                for start_date, end_date in employee.vacations:
                    print(f'\tFrom {start_date} to {end_date}')
