from django.db import models
from datetime import datetime
class Employee(models.Model):
    cat = [
        ('intern','intern'),
        ('developer','developer')

    ]

    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    atttendancetime = models.TimeField(auto_now_add=True)
    category = models.CharField( max_length=50, null = True,blank=True,choices = cat)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Attendance'

class Time(models.Model):
    date = models.DateField()
    time = models.TimeField(null = True)
    created = models.DateTimeField(default = datetime.now)

class Login(models.Model):
    username = models.CharField(max_length=255)    
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
        