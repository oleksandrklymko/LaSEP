from datetime import datetime


class Employee:
    employee_id = 1

    def __init__(self, first_name, last_name, patronymic, age, date_of_birth, place_of_birth, home_address):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.age = age
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.home_address = home_address
        self.current_job = None
        self.job_start_date = None
        self.department = None
        self.enterprise = None
        self.salary = None
        self.job_positions = []
        self.vacations = []
        self.vacation_days = 0
        self.employee_id = self.__class__.employee_id
        self.__class__.employee_id += 1

    def __repr__(self):
        return self.first_name + ' ' + self.last_name

    def change_job(self, job, start_date=datetime.date(datetime.today())):
        if job in self.enterprise.jobs and self.current_job != job:
            if self.current_job:
                self.job_positions.append(self.current_job)
            self.job_start_date = start_date
            self.current_job = job
            self.salary = job.salary
            self.vacation_days = job.vacation_days
            return True
        return False

    def take_vacation(self, end, begin=datetime.date(datetime.today())):
        days = abs(int(str(end - begin).split(' ')[0]))
        members_on_vacation = self.department.members_on_vacation
        vacation_fit_in_days = days > self.vacation_days
        if not self.department or vacation_fit_in_days or self in members_on_vacation or len(members_on_vacation) >= 5:
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
        print(f'Current job position: \'{self.current_job}\', salary : {self.salary}')


