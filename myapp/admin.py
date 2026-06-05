from django.contrib import admin

# Register your models here.

from .models import employeeTable, studentTable, teacherTable
admin.site.register(studentTable)
admin.site.register(employeeTable)
admin.site.register(teacherTable)
