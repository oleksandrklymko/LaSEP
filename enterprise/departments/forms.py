from django import forms
from django.forms import ValidationError

from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['jobs', 'job_starting_date', 'days_on_vacation']

    def clean_department(self):
        department = self.cleaned_data['department']
        if department and department.members.count() >= 20:
            raise ValidationError(f'There already 20 employees in {department} - department')

        return department


class ChangeEmployeeJobForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['job']

    def clean_job(self):
        job = self.cleaned_data['job']
        if self.instance.job == job:
            raise ValidationError(f'Employee {self.instance} already works as {job}')

        return job


class DepartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['head_of_department'].queryset = Employee.objects.filter(department=None)

    class Meta:
        model = Department
        fields = '__all__'


class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = '__all__'

    def clean(self):
        super(VacationForm, self).clean()
        days_in_vacation = self.cleaned_data['ending_date'] - self.cleaned_data['starting_date']
        employee = self.cleaned_data['employee']
        if days_in_vacation.days > employee.job.vacation_days:
            raise ValidationError('You don\'t have such amount of days for vacation')
        employee.days_on_vacation += days_in_vacation.days
        employee.save()

    def clean_starting_date(self):
        starting_date = self.cleaned_data['starting_date']
        employee_department = self.cleaned_data['employee'].department
        employees_count = 0
        vacations = Vacation.objects.filter(starting_date__lte=starting_date, ending_date__gte=starting_date)
        for item in vacations:
            if item.employee.department == employee_department:
                employees_count += 1
        if employees_count >= 5:
            raise ValidationError('5 Employees already on vacation at this dates')
        return starting_date


