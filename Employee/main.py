from enterprise import Enterprise
from departement import Department
from job import Job
from employee import Employee

from datetime import date

lasoft = Enterprise('LaSoft')

webdev = Department('Web Development', 'WebDev')

sofware = Job('Software Engineer', 20000, 14)

alex = Employee('Alex', 'Klymko', 'Vasylovich', 21, '14.08.1999', 'Lviv', 'Bla')

lasoft.add_department(webdev)
lasoft.add_employee(alex)
webdev.add_employee(alex)
webdev.change_leader(alex)
lasoft.add_job_position(sofware)
alex.change_job(sofware, date(2019, 11, 1))
alex.take_vacation(date(2020, 10, 25))
print(alex.vacations)
lasoft.show_department_employees(webdev)

webdev.increase_employee_salary(alex)
alex.show_information()

webdev.show_information_about_vacations()



