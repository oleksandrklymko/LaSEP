from employee import Employee
from departement import Department, show_department_employees
from job_position import Job
from datetime import date



alex = Employee('Alex', 'Klymko', 'Vasylovich', 21, '14.08.1999', 'Zhovkva', 'Dovbusha 73')
alex2 = Employee('Bohdan', 'Klymko', 'Vasylovich', 21, '14.08.1999', 'Zhovkva', 'Dovbusha 73')
dep1 = Department('LaSoft', 'LS')
programmer = Job('Programmer', 9000, 21)
devops = Job('DevOps', 12000, 14)
dep1.add_employee(alex)
dep1.add_employee(alex2)
alex.change_job_position(programmer)
alex.take_vacation(date(2020, 11, 12))
show_department_employees(dep1)
alex.show_information()
dep1.change_leader(alex)

Department.show_information_about_departments()
Employee.show_information_about_vacations()
