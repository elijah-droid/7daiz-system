from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'Branch', 'is_admin')

admin.site.register(Employee, EmployeeAdmin)
