from django.contrib import admin

from .models import *

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(Vacation)
