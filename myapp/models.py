from django.db import models

# Create your models here.
class studentTable(models.Model):
    name=models.CharField(null=True, max_length=100 , blank=True)
    age=models.IntegerField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    course=models.CharField(null=True, max_length=100, blank=True)

class employeeTable(models.Model):
    name=models.CharField(null=True, max_length=100 , blank=True)
    age=models.IntegerField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    
class teacherTable(models.Model):
    name = models.CharField(null=True, max_length=100 , blank=True)
    subject = models.CharField(null=True, max_length=100, blank=True)
    phone = models.CharField(null=True, max_length=15, blank=True)