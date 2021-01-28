from django.contrib import admin
from test_app.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']


admin.site.register(Employee, EmployeeAdmin)
