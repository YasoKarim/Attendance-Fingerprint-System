from django.contrib import admin
from .models import Employee,Time, Login


admin.site.register(Employee)
# Register your models here.
admin.site.register(Time)
admin.site.register(Login)