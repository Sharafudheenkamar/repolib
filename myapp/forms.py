from django.forms import ModelForm
from .models import studentTable, employeeTable

class StudentForm(ModelForm):
    class Meta:
        model = studentTable
        fields = ['name', 'age', 'email']

class EmployeeForm(ModelForm):
    class Meta:
        model = employeeTable
        fields = ['name', 'age', 'email']