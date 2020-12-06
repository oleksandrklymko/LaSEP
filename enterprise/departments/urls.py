from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('department/new', views.create_department, name='create_department'),
    path('department/<int:pk>/', views.department_members, name='department_members'),
    path('employees/', views.employees, name='employees'),
    path('employees/new/', views.create_employee, name='add_employee'),
    path('employees/<int:pk>/change_job/', views.change_employee_job, name='change_job'),
    path('vacations/', views.vacations, name='vacations'),
    path('vacations/new/', views.add_vacation, name='add_vacation'),
    path('vacations/employee/<int:pk>/', views.employees_vacations, name='vacations_info')
]
