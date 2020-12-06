from datetime import datetime
from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=100)
    title_abbreviation = models.CharField(max_length=10)
    head_of_department = models.OneToOneField('Employee',
                                              related_name='head_of_department',
                                              on_delete=models.SET_NULL,
                                              null=True,
                                              blank=True
                                              )

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    id_code = models.CharField(max_length=13, unique=True)
    date_of_birth = models.DateTimeField()
    place_of_birth = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    department = models.ForeignKey(Department, related_name='members', on_delete=models.SET_NULL, null=True, blank=True)
    job = models.ForeignKey('Job', related_name='+', on_delete=models.CASCADE, null=True)
    days_on_vacation = models.IntegerField(default=0)
    job_starting_date = models.DateTimeField(null=True)
    jobs = models.ManyToManyField('Job')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def calculate_salary(self):
        years_at_work = datetime.now().year - self.job_starting_date.year
        salary = self.job.salary
        if years_at_work <= 1:
            return self.job.salary
        else:
            for i in range(years_at_work):
                salary += salary * 1.2 / 100
            return int(salary)


class Job(models.Model):
    title = models.CharField(max_length=50)
    salary = models.IntegerField()
    vacation_days = models.IntegerField()

    def __str__(self):
        return self.title


class Vacation(models.Model):
    employee = models.ForeignKey(Employee, related_name='vacations', on_delete=models.CASCADE)
    starting_date = models.DateField()
    ending_date = models.DateField()

    def __str__(self):
        return f'{self.employee}, starting date - {self.starting_date}, ending date - {self.ending_date}'
