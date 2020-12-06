from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now

from .models import Department, Employee, Job, Vacation
from .forms import EmployeeForm, DepartmentForm, ChangeEmployeeJobForm, VacationForm


def index(request):
    departments = Department.objects.all()
    return render(request, 'departments/index.html', {'departments': departments})


def department_members(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'departments/department_members.html', {'department': department})


def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['head_of_department']:
                employee = Employee.objects.get(pk=form.cleaned_data['head_of_department'].id)
                form.save()
                employee.department = Department.objects.get(head_of_department=employee)
                employee.save()
            form.save()
            return redirect('index')
    else:
        form = DepartmentForm()
    return render(request, 'departments/new_department.html', {'form': form})


def employees(request):
    employees = Employee.objects.all()
    return render(request, 'departments/employees.html', {'employees': employees})


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            employee = Employee.objects.get(id_code=form.cleaned_data['id_code'])
            if employee.department:
                employee.job_starting_date = now()
                employee.save()
            return redirect('employees')
    else:
        form = EmployeeForm()
    return render(request, 'departments/new_employee.html', {'form': form})


def change_employee_job(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee_prev_job = employee.job
    if request.method == 'POST':
        form = ChangeEmployeeJobForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            employee.job_starting_date = now()
            employee.jobs.add(employee_prev_job)
            employee.save()
            return redirect('employees')
    else:
        form = ChangeEmployeeJobForm(instance=employee)

    return render(request, 'departments/change_job.html', {'form': form})


def vacations(request):
    employees = Employee.objects.all()
    return render(request, 'departments/vacations.html', {'employees': employees})


def employees_vacations(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'departments/vacations_info.html', {'employee': employee})


def add_vacation(request):
    if request.method == 'POST':
        form = VacationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacations')
    else:
        form = VacationForm()
    return render(request, 'departments/new_vacation.html', {'form': form})
