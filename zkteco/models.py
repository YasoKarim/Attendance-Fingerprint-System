from django.db import models
from datetime import datetime

class UserModel(models.Model):

    uid = models.IntegerField()
    name = models.CharField(max_length=255)
    #department = models.CharField(max_length=255)
    #position = models.CharField(max_length=255)

    def __str__(self):
        return f"User {self.uid}: {self.name}"


class AttendanceModel(models.Model):

    employee_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    attendance_status = models.CharField(max_length=255)

    def __str__(self):
        return f"Attendance for {self.employee_id} on {self.date} at {self.time}"


















'''
class Emp(models.Model):
    empName = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    dateTimeField = models.DateTimeField()

class User(models.Model):
    name = models.CharField(max_length=255,null=True)
    #user_id = models.IntegerField(unique=True) 
    timestamp = models.DateField(null=True)
    status = models.CharField(max_length=255,null=True)

    #def __str__(self):
    #   return self.name
    
class Attendance(models.Model):
    user_id = models.IntegerField(primary_key=True)
    uername = models.CharField(max_length=50)
    
    time_in = models.TimeField(null=True)
    time_out = models.TimeField(null=True)
'''
